import datetime
from web_scrape import *

raw = formatted('https://uwaterloo.ca/registrar/important-dates/list?academic_year=229&date=All&page=1')

def format_time(time):
    ''' formats time into datetime parsable object '''
    time = time[:12]
    year = time[-4:]
    time_a = time.split(',')[0].split(' ')
    day = ('0'+time_a[1])[-2:]

    m = time[:3]
    if m == 'Jan':
        month = '01'
    elif m == 'Feb':
        month = '02'
    elif m == 'Mar':
        month = '03'
    elif m == 'Apr':
        month = '04'
    elif m == 'May':
        month = '05'
    elif m == 'Jun':
        month = '06'
    elif m == 'Jul':
        month = '07'
    elif m == 'Aug':
        month = '08'
    elif m == 'Sep':
        month = '09'
    elif m == 'Oct':
        month = '10'
    elif m == 'Nov':
        month = '11'
    else:
        month = '12'

    return (year+'-'+month+'-'+day+' 00:00:00')
    
def str_to_dt(str_time):
    ''' formats [[name, time], [name, time]] into proper format'''
    for i in str_time:
        i[1] = format_time(i[1])
    return str_time

def next_month(ym):
    ''' returns numerical value of next month '''
    if ym[5:7] == '12':
        y = str(int(ym[:4]) + 1)
        m = '01'
        return (y+'-'+m)
    else:
        y = ym[:4]
        m = str(int(ym[5:7]) + 1)
        return (y+'-'+m)

def find_nearest(dt_raw):
    ''' finds the nearest event to today in dt_raw '''
    today = str(datetime.datetime.today())[:-7]
    for i in range(len(dt_raw)):
        if dt_raw[i][1][:7] == today[:7]:
            if (int(today[8:10]) <= int(dt_raw[i][1][8:10])):
                return dt_raw[i]
        elif dt_raw[i][1][:7] == next_month(today[:7]):
            return dt_raw[i]

def format_nearest(inputt):
    ''' formats input '''
    string = ''
    string = 'The nearest event is ' + string + '**' + inputt[0] + '** ' + inputt[1][:10] + '.'
    return string

