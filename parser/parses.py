import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import csv

value_list1 = []
value_list2 = []
HEADERS = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.686 Yowser/2.5 Safari/537.36'}


def parser():
    URL = 'https://stackoverflow.com/tags'
    response = requests.get(URL, headers=HEADERS)
    soap = bs(response.content, 'html.parser')
    items = soap.find_all('div', class_='s-card')

    for item in items:
        try:
            value_list2.append({item.find('a', class_ = "post-tag").get_text(strip = True):item.find('div', class_ = "mt-auto d-flex jc-space-between fs-caption fc-black-400").get_text().split()[0]})
        except AttributeError:
            continue
    return(value_list2)


def tag_parse(link):
    thousand = lambda x:int(x[:x.index('k')])*1000 if 'k' in x else int(x)
    pattern_id = re.compile('question-summary-(\d*)')
    pattern_views = re.compile('(\d*k*) views')
    pattern_answer = re.compile('(\d*)answer')
    values_1 = list()

    response = requests.get(link, headers=HEADERS)
    soap = bs(response.content, 'html.parser')
    items = soap.find_all('div', class_='question-summary')
    for item in items:
        try:
            answers_accepted = False
            answers = 0
            try:
                answers = int(pattern_answer.search(item.find('div',class_='answered').get_text())[1])
            except AttributeError:
                pass
            try:
                answers = int(pattern_answer.search(item.find('div', class_='answered-accepted').get_text())[1])
                answers_accepted = True
            except AttributeError:
                pass

            vote = item.find('span',class_='vote-count-post')
            views = item.find('div', class_ ='views')
            values_1.append({pattern_id.search(item['id'])[1]:{'vote':int(vote.get_text()),'answer':answers,'views': thousand(pattern_views.search(views.get_text())[1]),'accepted' : answers_accepted}})
        except AttributeError:
            continue

    return values_1
def dataframe_data(link):
    dfx = tag_parse(link)
    index_data,  colls, list_4_df_data = [],[],[]

    for _ in dfx:
        index_data.append((list(_.keys())[0]))
        colls = list(_[(list(_.keys())[0])].keys())
        list_4_df_data.append(list(_[(list(_.keys())[0])].values()))


    df = pd.DataFrame(list_4_df_data,index=index_data,columns=colls)

    df.reset_index(inplace=True)
    df.rename(columns= {'index':'id'}, inplace=True)
    return df
def dataframe_tags():
    tags = parser()
    index_tags, colls_tags, list_4_df_tags = [],[],[]
    for x in tags:
        list_4_df_tags.append(list(x.values())[0])
        index_tags.append(list(x.keys())[0])
        colls_tags = ['views']

    df_tags = pd.DataFrame(list_4_df_tags,index=index_tags,columns=colls_tags)

    df_tags.reset_index(inplace=True)

    df_tags.rename(columns={'index': 'tags'}, inplace=True)
    return df_tags
current_tag = 'javascript'
for x in range(1,3):
    csv_export = dataframe_data(f'https://stackoverflow.com/questions/tagged/{current_tag}?tab=active&page={x}&pagesize=50')

    csv_export.to_csv(f'{current_tag}_{x}.csv')


