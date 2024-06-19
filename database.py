import pyodbc


class Data:
    def __init__(self, road):
        self.static_road = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + road
        self.conn = pyodbc.connect(self.static_road)

    def insert_player(self, players: list):
        sql_insert = """
                       Insert into Players (PlayerID_EXT,F,I,F_eng,I_eng,PlayerID_EXT_Str)
                       VALUES (?,?,?,?,?,?)
                     """
        cursor = self.conn.cursor()
        # Проверяем есть ли Игрок в БД
        for player in players:
            check = self.select_player_id_by_ext(player['player_id_ext'])
            if check:
                continue

            cursor.execute(sql_insert, (
                player['player_id_ext'], player['player_surname'].upper(), player['player_name'].lower().capitalize(),
                player['player_surname'].upper(),
                player['player_name'].lower().capitalize(), player['player_str_ext']))
        cursor.commit()
        cursor.close()

    def set_par_zaezd(self, pars: list):
        cursor = self.conn.cursor()

        sql_update = """
                    UPDATE Zaezd SET ZaezdYDAR = ? WHERE ZaezdNumber = ?
                     """
        for number in range(len(pars)):
            cursor.execute(sql_update, (pars[number], number + 1))

        cursor.commit()
        cursor.close()

    def insert_in_zaezdMaps(self, players: list):
        # Проверяем есть ли там уже игроки
        cursor = self.conn.cursor()

        sql_select_zaezd = """
                                SELECT ZaezdID FROM Zaezd
                           """
        sql_insert_zaezdmaps = """
                                    INSERT INTO ZaezdMaps (ZaezdID,ZaezdPlayerID,ZaezdDate) VALUES (?,?,?)
                               """
        zaezds = [i[0] for i in cursor.execute(sql_select_zaezd).fetchall()]
        for player in players:
            player_id = self.select_player_id_by_ext(player['player_id_ext'])
            for zaezd in zaezds:
                try:
                    cursor.execute(sql_insert_zaezdmaps, (zaezd, player_id, player['player_date']))
                except pyodbc.IntegrityError:
                    continue

        cursor.commit()
        cursor.close()

    def select_player_id_by_ext(self, id_ext: str):
        cursor = self.conn.cursor()

        sql = """
                                        SELECT PlayerID FROM Players Where PlayerID_EXT = ?
                                      """

        temp_res = cursor.execute(sql, id_ext)
        res = temp_res.fetchone()
        if res:
            return res[0]
        else:
            return None

    def clear_database(self):
        cursor = self.conn.cursor()
        tables = ('ZaezdMaps',)
        for table in tables:
            sql = f"""Delete from {table}"""
            cursor.execute(sql)

        self.conn.commit()
