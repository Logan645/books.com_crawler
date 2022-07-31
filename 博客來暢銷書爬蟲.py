import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
url="https://www.books.com.tw/web/sys_saletopb/books/?attribute=30"
response=requests.get(url) #取得網頁內容
soup=BeautifulSoup(response.text ,'html.parser') #建立beautifulsoap物件
catalog=soup.find_all('div','type02_bd-a')
# print(catalog)
import csv
with open('博客來暢銷書top100.csv','w',encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['書名','作者','價格'])
    for i in catalog:
        bookname = i.find('h4').a.text.strip() #爬取書名
        # print(bookname)
        try:
            writer=i.find_all('li')[0].a.text.strip() #爬取作者
            writer=writer
            # print(writer)
        except AttributeError:
            writer=None
            # print(writer)
        price=i.find_all('b')[-1].text #取得價格
        # print(price)
        # print('書名：{}；作者：{}；價格：${}'.format(bookname, writer,price))
        csv_writer.writerow([bookname, writer, price])