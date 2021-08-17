#################### html에서 제목 불러들이기
import sys
from bs4 import BeautifulSoup

html_file = open('html_file.html','r', -1, "UTF-8") # html_file 읽어들이기
read_html = html_file.read()

soup = BeautifulSoup(read_html, 'html.parser')

for i in range(0,100):
    my_data = soup.select(
        '#mArticle > div.box_headline > ul:nth-child(3) > li:nth-child(2) > strong'
        #'.hdline_news .list'
        # '#content-area #group-area #cafe-menu .box-g-m #group1734 li a',
        # '#content-area #group-area #cafe-menu .box-g-m #group1735 li a',
        # '#content-area #group-area #cafe-menu .box-g-m #group1736 li a',
        # '#content-area #group-area #cafe-menu .box-g-m #group1737 li a',
        # '#content-area #group-area #cafe-menu .box-g-m #group1738 li a'
        # '#content-area #group-area #cafe-menu .box-g-m #group1739 li a'
    )
print(my_data)
print(type(my_data))

qustn = open("data/title.txt","w", -1 , "UTF-8")

for i in my_data:
    qustn.write(i.text.strip())
    qustn.write("\n")
#    print(i.text.strip()) # strip()  : 공백제거문 (문자열 뒤에만 사용 가능)

qustn.close()
'''

url = []

qustn2 = open("data/url.txt","w", -1 , "UTF-8")
for i in my_data:
    qustn2.write('https://news.daum.net/'+i.attrs['href']) # 경로 설정
    qustn2.write('\n')
qustn2.close()
'''