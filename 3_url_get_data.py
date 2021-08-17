import sys
from urllib.request import urlopen
import datetime
#파일명을 만들때 날짜와 시간으로 구분해서 만들기 위함

news_url = open('data/url.txt','r')
news_url_arr = news_url.read().split("\n")
news_url_arr.pop() # 맨 마지막에 있는 리스트 제거 

num = 0 
for i in news_url_arr:
    num = num + 1
    f = urlopen(i)
    encoding = f.info().get_content_charset(failobj="utf-8")
    text = f.read().decode(encoding)
    html_file = open('data/' + str(num) +'_joonggonara_data.html','w', -1 , "UTF-8") 
    html_file.write(text)
    html_file.close

print(news_url_arr)
