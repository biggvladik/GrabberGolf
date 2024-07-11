import pyodbc


class Data:
    def __init__(self, road):
        self.static_road = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + road
        self.conn = pyodbc.connect(self.static_road)

    def insert_player(self, players: list):
        sql_insert = """
                       Insert into Players (PlayerID_EXT,F,I,F_eng,I_eng,PlayerID_EXT_Str,ClassID)
                       VALUES (?,?,?,?,?,?,?)
                     """
        cursor = self.conn.cursor()

        # Проверяем есть ли Игрок в БД
        for player in players:
            check = self.select_player_id_by_ext(player['player_id_ext'])
            if check:
                continue
            class_id = self.select_id_from_classes(player['player_class'])
            cursor.execute(sql_insert, (
                player['player_id_ext'], player['player_surname'].upper(), player['player_name'].lower().capitalize(),
                player['player_surname'].upper(),
                player['player_name'].lower().capitalize(), player['player_str_ext'], class_id))
        cursor.commit()
        cursor.close()

    def set_par_zaezd(self, pars: list):
        cursor = self.conn.cursor()

        sql_update = """
                    UPDATE Zaezd SET ZaezdYDAR = ? WHERE ZaezdCountNum = ?
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
                                    INSERT INTO ZaezdMaps (ZaezdID,ZaezdPlayerID,ZaezdDate,ZaezdPlayerPosition) VALUES (?,?,?,?)
                               """
        zaezds = [i[0] for i in cursor.execute(sql_select_zaezd).fetchall()]
        for player in players:
            player_id = self.select_player_id_by_ext(player['player_id_ext'])
            for zaezd in zaezds:
                try:
                    cursor.execute(sql_insert_zaezdmaps, (zaezd, player_id, player['player_date'], player['player_number']))
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
        tables = ('ZaezdMaps', 'Players')
        for table in tables:
            sql = f"""Delete from {table}"""
            cursor.execute(sql)

        self.conn.commit()

    def select_id_from_classes(self, classname: str):
        cursor = self.conn.cursor()

        sql = """
                   SELECT ClassID FROM Classes WHERE ClassName_Ext = ?
                 """

        cursor.execute(sql, classname)
        res = cursor.fetchone()
        if res != None:
            cursor.close()
            return res[0]

        sql_max_id = """
                        SELECT MAX(ClassID) FROM Classes
                     """
        max_id = cursor.execute(sql_max_id).fetchone()
        if max_id:
            max_id = max_id[0] + 1
        else:
            max_id = 1
        sql_insert = """
                        Insert into Classes  (ClassID,ClassName,ClassName_Ext)
                                   VALUES (?,?,?)
                     """
        cursor.execute(sql_insert, (max_id, classname, classname))

        cursor.commit()
        cursor.close()
        return max_id

    def update_score_players(self, players: list):
        cursor = self.conn.cursor()
        columns = [f'Netto{count}' for count in range(1, 19)]
        s = ' = ?, '.join(columns) + ' = ?' + ', NettoTotal = ? '
        sql = """
                UPDATE Players SET 
              """ + s + """  WHERE PlayerID_EXT = ?"""
        for player in players:
            columns = tuple(
                [player[f'point_{count}'] for count in range(1, 19)] + [player['pts']] + [player['player_id_ext']])
            cursor.execute(sql, columns)
        cursor.commit()

    def select_zaezd_id_by_number(self, number: int):
        cursor = self.conn.cursor()
        sql = "SELECT ZaezdID from Zaezd WHERE ZaezdCountNum = ?"
        res = cursor.execute(sql, number).fetchone()[0]
        cursor.close()
        return res

    def update_zaezdmaps_score(self, players: list):
        cursor = self.conn.cursor()
        zaezd_keys = {f'zaezd{count}': self.select_zaezd_id_by_number(count) for count in range(1, 19)}
        sql_update_zaezdmaps = """
                                 UPDATE ZaezdMaps SET ZaezdPlayerTimeInt = ? , ZaezdPlayerPoints = ?  WHERE ZaezdID = ? AND ZaezdPlayerID = ?
                              """
        for player in players:
            player_id = self.select_player_id_by_ext(player['player_id_ext'])
            for count in range(1, 19):
                zaezd_id = zaezd_keys[f'zaezd{count}']
                cursor.execute(sql_update_zaezdmaps,
                               (player[f'shot_{count}'], player[f'point_{count}'], zaezd_id, player_id))
        cursor.commit()
        cursor.close()

    def update_score_logs(self, events: list):
        cursor = self.conn.cursor()

        zaezd_keys = {f'zaezd{count}': self.select_zaezd_id_by_number(count) for count in range(1, 19)}
        for event in events:
            player_id = self.select_player_id_by_ext(event['player_id_ext'])

            sql_update = """
                            UPDATE ZaezdMaps SET ZaezdPlayerTimeInt = ?, ZaezdPF = ? WHERE ZaezdID = ? AND ZaezdPlayerID = ?
                         """
            cursor.execute(sql_update, event['point'], event['status'], zaezd_keys[f"zaezd{event['number_hole']}"], player_id)
            print(f"player_id: {event['player_id_ext']}, лунка: {event['number_hole']},status:{event['status']}")
        cursor.commit()
        cursor.close()

# data = Data('D:\\database\\Golf_2022.mdb')
# from factory import get_stat_log
# q = get_stat_log('https://ligastavok.livescoring.ru/nakhabino2024/log.txt')
# data.update_score_logs(q)
