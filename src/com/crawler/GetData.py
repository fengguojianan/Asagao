import urllib
import urllib.request
import requests
import selenium
import lxml
import pymysql
import pymongo
import redis

urllib.request.urlopen('http://www.baidu.com')
requests.get('http://www.baidu.com')
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.get('https://www.google.com')
driver.page_source

driver=webdriver.PhantomJS()
driver.get('http://www.baidu.com')
driver.page_source

from bs4 import  BeautifulSoup
soup=BeautifulSoup('<html></html>','lxml')
print (soup)

from pyquery import PyQuery as pq
doc=pq('<html></html>')
doc=pq('<html>Hello</html>')
result=doc('html').text()
result

conn=pymysql.connect(host='localhost',user='root',password='zxccxz',port=3306,db='study')
cursor=conn.cursor()
cursor.execute('select * from task')
cursor.fetchone()


client=pymongo.MongoClient('localhost')
db=client['testdb']
db['table'].insert({'name':'bob'})
db['table'].find_one({'name':'bob'})

r=redis.Redis('localhost',6379)
r.set('name','bob')
r.get('name')






