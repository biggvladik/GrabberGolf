import traceback

import requests

def get_stat(url:str):
    q = requests.get(url,timeout=3).text.split('\n')

    par_line = q[0].split(';')
    par = [i for i in par_line[5:len(par_line) - 4] if i != '']

    players = []

    for player_item in q[1::]:
        d = {}
        if player_item == '':
            continue
        try:
            d['player_id_ext'] = player_item.split(';')[0]
            d['player_name'] = player_item.split(';')[1].split()[1]
            d['player_surname'] = player_item.split(';')[1].split()[0]
            d['player_class'] = player_item.split(';')[2]
            d['player_date'] = player_item.split(';')[4]
            d['player_str_ext'] = player_item.split(';')[1]

            points = player_item.split(';')[5::]
            count = 1
            for number in range(0, len(points) - 4, 2):
                d[f'shot_{count}'] = (lambda x: 0 if x == '' else x)(points[number])
                d[f'point_{count}'] = (lambda x: 0 if x == '' else x)(points[number+1])
                count += 1
            d['pts'] = (lambda x: 0 if x == '' else x)(points[-2])
            players.append(d)
        except:
            print(traceback.format_exc())
            continue
    return par,players

# from database import Data
# database = Data('D:\\database\\Golf_2022.mdb')
#
# q = get_stat('https://ligastavok.livescoring.ru/pestovo2023/export.txt')
#
# for i in q[1]:
#     print(i)
#database.insert_player(q[1])
#
# database.set_par_zaezd(q[0])
# database.insert_in_zaezdMaps(q[1])





def get_stat_test(q):
    q = q.split('\n')

    par_line = q[0].split(';')
    par = [i for i in par_line[5:len(par_line) - 4] if i != '']

    players = []

    for player_item in q[1::]:
        d = {}
        if player_item == '':
            continue
        d['player_id_ext'] = player_item.split(';')[0]
        d['player_name'] = player_item.split(';')[1].split()[1]
        d['player_surname'] = player_item.split(';')[1].split()[0]
        d['player_class'] = player_item.split(';')[2]
        d['player_date'] = player_item.split(';')[4]
        d['player_str_ext'] = player_item.split(';')[1]

        points = player_item.split(';')[5::]
        count = 1
        for number in range(0, len(points) - 4, 2):
            d[f'shot_{count}'] = (lambda x: 0 if x == '' else x)(points[number])
            d[f'point_{count}'] = (lambda x: 0 if x == '' else x)(points[number+1])
            count += 1
        d['pts'] = (lambda x: 0 if x == '' else x)(points[-2])
        players.append(d)
    return par,players







def get_stat_log(url:str):
    q = requests.get(url, timeout=3).text.split('\n')



    events = []

    for player_item in q:
        d = {}
        if player_item == '':
            continue
        try:
            d['player_id_ext'] = player_item.split(';')[1]
            d['number_hole'] = (lambda x: 0 if x == '' else x)(player_item.split(';')[4])
            d['point'] = (lambda x: 0 if x == '' else x)(player_item.split(';')[5])
            d['status'] = player_item.split(';')[6]
            events.append(d)
        except:
            continue
    print(events)
    return events




get_stat_log('https://ligastavok.livescoring.ru/nakhabino2024/log.txt')
# f = open('test.txt',encoding='utf-8')
# q = f.read()
#
# print(get_stat_test(q))


