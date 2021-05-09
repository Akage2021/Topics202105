#抽出したあとセブンイレブンのみにしたもの。ファミマなどの求人も将来使うかもしれないので、一旦このコードは使わない。
import csv
import time
import urllib
import requests
import pprint
import random
from bs4 import BeautifulSoup

place_list=[]
store_list=[]
daytime_list=[]
item_list = []

alfa=740301 #640000からは1万件単位でスクレイピング（それまでは1000件単位）してみる。⇒１回ごとにjupyterに入りなおしが必要。
#1月6日段階では745012まで求人あり
#次はいま記載しているコードを動かすことから（前回はrangeの後を10000にしていなくて失敗した）
for i in range(10):
    request_interval =2 # ページ取得間隔
    load_url = 'https://convini.shotworks.jp/work/{}'.format(alfa)
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    place=soup.find_all("td",class_="p-data-table__item")[24]
    place_t_a=place.text
    place_t_b=place_t_a.replace("\n","")
    place_t_c=place_t_b.replace(" ","")
    place_t=place_t_c.replace("MAP","")
    place_list.append([place_t]) 
    
    store=soup.find("div",class_="work-box__store__name")
    store_t_a=store.text
    store_t_b=store_t_a.replace("\n","")
    store_t=store_t_b.replace(" ","")
    store_list.append([store_t])
    
    daytime=soup.find_all("td",class_="p-data-table__item")[0]
    daytime_t_a=daytime.text
    daytime_t_b=daytime_t_a.replace("\n","")
    daytime_t=daytime_t_b.replace(" ","")
    daytime_list.append([daytime_t])
    
    alfa+=1
    
    time.sleep(request_interval)
    
#pprint.pprint(place_list)
#pprint.pprint(store_list)
#pprint.pprint(daytime_list)


import pandas as pd
import datetime as dt
from datetime import datetime, date, timedelta

df=pd.DataFrame([place_list,store_list,daytime_list],index=['住所','店舗名','募集日'])
df_711=df.T
df_711

#df_711.to_csv('sw_list_730001_740000.csv', encoding="utf_8_sig", index=False)