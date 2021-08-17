######################## 홈페이지에서 html 긁어오기
from urllib.request import urlopen
import sys

f = urlopen('https://news.daum.net/')

encoding = f.info().get_content_charset(failobj="utf-8")
text = f.read().decode(encoding)
html_file = open('html_file.html','w',-1,'UTF-8')  #  f를 html 파일로 긁어오기

html_file.write(text)
html_file.close