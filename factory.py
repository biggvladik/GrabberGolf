import traceback
import requests
from datetime import datetime

def get_stat(url:str):
    q = requests.get(url,timeout=3).text.split('\n')

    par_line = q[0].split(';')
    par = [i for i in par_line[5:len(par_line) - 4] if i != '']

    players = []

    for number,player_item in enumerate(q[1::]):
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
            d['player_number'] = number+1
            points = player_item.split(';')[5::]
            count = 1
            for number in range(0, len(points) - 4, 2):
                d[f'shot_{count}'] = points[number]
                d[f'point_{count}'] = points[number+1]
                count += 1
            d['pts'] = (lambda x: 0 if x == '' else x)(points[-2])
            d['pts_sum'] = (lambda x: 0 if x == '' else x)(points[-1])
            players.append(d)
        except:
            print(traceback.format_exc())
            continue
    return par,players

def get_stat_log(url:str,flag):
    q = requests.get(url, timeout=3).text.split('\n')[::-1]
    events = []
    update_stat = []
    for player_item in q:
        d = {}
        if player_item == '':
            continue
        try:

            d['player_id_ext'] = player_item.split(';')[1]
            d['number_hole'] = (lambda x: 0 if x == '' else x)(player_item.split(';')[4])
            d['point'] = (lambda x: 0 if x == '' else x)(player_item.split(';')[5])
            d['status'] = player_item.split(';')[6]
            if check_update_item(update_stat,d):
                events.append(d)
                update_stat.append(d)
        except:
            continue
    if flag == 'all':
        return events
    print('ДЛИНА ЛОГА,',len(events[len(events)-int(flag)::]))
    return events[len(events)-int(flag)::]

def check_update_item(data:list,item:dict):
    for s in data:
        if s['number_hole'] == item['number_hole'] and s['player_id_ext'] == item['player_id_ext']:
            return False

    return True






def get_stat_gross(url:str):
    q = requests.get(url,timeout=3).text.split('\n')

    par_line = q[0].split(';')
    par = [i for i in par_line[4:len(par_line) - 2] if i != '']

    players = []

    for number,player_item in enumerate(q[1::]):
        d = {}
        if player_item == '':
            continue
        try:
            d['player_id_ext'] = player_item.split(';')[0]
            d['player_name'] = player_item.split(';')[1].split()[1]
            d['player_surname'] = player_item.split(';')[1].split()[0]
            d['player_class'] = player_item.split(';')[2]
            d['player_str_ext'] = player_item.split(';')[1]
            d['player_number'] = number+1
            d['player_date'] = datetime.now().strftime('%d.%m.%Y')
            points = player_item.split(';')[4::]
            count = 1
            for number in range(0, len(points) - 2):
                d[f'point_{count}'] = points[number]
                count += 1
            d['pts'] = (lambda x: 0 if x == '' else x)(points[-2])
            d['pts_sum'] = (lambda x: 0 if x == '' else x)(points[-1])
            players.append(d)
        except:
            print(traceback.format_exc())
            continue
    return par,players


def convert_point(point):
    if point == '' or point == ' ':
        return 0
    return point

#print(get_stat_gross('https://agr.livescoring.ru/champ32/export.txt'))








#print(get_stat('https://ligastavok.livescoring.ru/nakhabino2024/export.txt'))
