################### html에서 본문 내용 불러들이기
import sys
from urllib.request import urlopen
import datetime
from bs4 import BeautifulSoup
import re

for i in range(5):
    print(i+1)
    html_file = open('data/' + str(i+1) + '_daum_news.html','r',-1,'utf-8') 
    read_html = html_file.read()
    soup = BeautifulSoup(read_html, 'html.parser')
    my_data = soup.select(
        '#main-area div table tbody tr td.td_article div.board-list div a'
        ''
    )
    
    print(my_data)

    print(my_data[0].get_text())

    text_file = open('data_read/' + str(i) + '_daum_news.html','w',-1,'utf-8') 
    text_file.write(my_data[i+17].get_text().strip()) 
    text_file.close()