import requests
from bs4 import BeautifulSoup

# URLS
main_url = 'https://uwaterloo.ca/registrar/important-dates/list?academic_year=229&date=All&page=0'

def next_page():
    ''' modifies the url to point to the next page '''
    global main_url
    
    old_index = int(main_url[-1:])
    new_index = old_index + 1
    new_url = main_url[:-1] + str(new_index)
    main_url = new_url
    return formatted(new_url)

def nextp():
    next_page()
    current_page()


def prev_page():
    ''' modifies the url to point to the previous page '''
    global main_url
    
    old_index = int(main_url[-1:])
    if old_index <= 0:
        new_index = old_index
    else:
        new_index = old_index - 1
    new_url = main_url[:-1] + str(new_index)
    
    main_url = new_url
    return formatted(new_url)

def prevp():
    prev_page()
    current_page()


def html_parsing(html):
    ''' given the html for one table row, will parse into [name, date] form '''
    html = str(html)
    name = html.split('<td>')[1].split('<a class="uw-imp-dates-loader" ')[1].split('>')[1].split('<')[0]
    date = html.split('<td>')[-1].split('<')[0]
    return [name, date]

def retrieve_site_data(url):
    ''' retrieve html data from url '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.select('tbody tr')  
    return html

def formatted(url):
    ''' formats url data '''
    lst = []
    data = retrieve_site_data(url)
    for row in data:
        lst.append(html_parsing(row))
    return lst

def current_page():
    ''' current page '''
    #return (formatted(main_url))
    string = ''
    for i in formatted(main_url):
        string = string + '**' + i[0] + '**' + '\t' + i[1] + '\n'

    return string

def reset_page_count():
    global main_url
    main_url = main_url[:-1] + '0'

def helpme():
    ''' returns list of all commands '''
    s = open('helpme.txt', 'r')
    return s.read()
