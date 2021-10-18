import requests
from bs4 import BeautifulSoup as bs
import re

test_dict = {'python': {'vote': 16, 'answered_accepted': 28, 'question': 50,
                        'views': 200, 'answered': 50, 'req_amount': 500}}
value_list1 = []
value_list2 = []
HEADERS = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.686 Yowser/2.5 Safari/537.36'}


def parser():

    pattern = re.compile('(\d*) questions')
    URL = 'https://stackoverflow.com/tags'
    response = requests.get(URL, headers=HEADERS)
    soap = bs(response.content, 'html.parser')
    items = soap.find_all('div', class_='s-card')

    for item in items:
        try:
            value_list2.append({item.find('a', class_ = "post-tag").get_text(strip = True):item.find('div', class_ = "mt-auto d-flex jc-space-between fs-caption fc-black-400").get_text().split()[0]})
        except AttributeError:
            continue
    print(value_list2)


def tag_parse(link = None):
    values_dict = {}
    values_1 = list()
    URL = 'https://stackoverflow.com/questions/tagged/javascript?tab=active&page=1&pagesize=50'
    response = requests.get(URL, headers=HEADERS)
    soap = bs(response.content, 'html.parser')
    items = soap.find_all('div', class_='question-summary')
    for item in items:
        try:
            answers_accepted = False
            answers = 0
            try:
                answers = item.find('div',class_='answered').get_text()
            except AttributeError:
                pass
            try:
                answers = item.find('div', class_='answered-accepted').get_text()
                answers_accepted = True
            except AttributeError:
                pass

            vote = item.find('span',class_='vote-count-post')
            views = item.find('div', class_ ='views')
            values_1.append({item['id']:{'vote':vote.get_text(),'answer':answers,'views': views.get_text(),'accepted' : answers_accepted}})
        except AttributeError:
            continue

    print(values_1)
tag_parse()