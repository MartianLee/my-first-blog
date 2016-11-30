# -*- coding: utf-8 -*-

import urllib.request
import os, csv
import sqlite3
import json
import re
from bs4 import BeautifulSoup
#from urllib.request import urlopen


targetUrl = "http://sports.news.naver.com/wfootball/record/index.nhn"
r = urllib.request.urlopen(targetUrl).read()
soup = BeautifulSoup(r,"html.parser")
#print(soup)

####여기는 json
'''
response = urllib.request.urlopen(targetUrl)
data = json.loads(response.read())
print(data)
'''
text = soup.get_text()
extractedText = text[text.find("jsonTeamRecord"):text.find("sortedTeamRecord:")] # text.find("sortedTeamRecord")
print(extractedText)

regex = re.compile('"teamName":"[^,]+,')
clubKor = re.findall(regex,extractedText)
cnt = 0
for i in clubKor:
	clubKor[cnt] = i[12:-2]
	cnt+=1
print("clubKor :\n",clubKor)


regex = re.compile('"rank":[^,]+,')
position = re.findall(regex,extractedText)
cnt = 0
for i in position:
	position[cnt] = i[7:-1]
	cnt+=1
print("position :\n",position)


regex = re.compile('"gameCount":[^,]+,')
played = re.findall(regex,extractedText)
cnt = 0
for i in played:
	played[cnt] = i[12:-1]
	cnt+=1
print("played :\n",played)


regex = re.compile('won":[^,]+,')
win = re.findall(regex,extractedText)
cnt = 0
for i in win:
	win[cnt] = i[5:-1]
	cnt+=1
print("win :\n",win)

regex = re.compile('drawn":[^,}]+[,|}]')
draw = re.findall(regex,extractedText)
cnt = 0
for i in draw:
	draw[cnt] = i[7:-1]
	cnt+=1
print("draw :\n",draw)

regex = re.compile('lost":[^,]+,')
lose = re.findall(regex,extractedText)
cnt = 0
for i in lose:
	lose[cnt] = i[6:-1]
	cnt+=1
print("lose :\n",lose)




#editData = soup.find_all('span',{'class':"name"})
#"teamName"
editData = soup.find_all('span',{'class':"name"})
editDataStr = str(editData)
#print(editData)
#print(editDataStr)

#print(soup.get_text())
#print(' ')


# SQLite DB 연결
conn = sqlite3.connect("db.sqlite3")
 
# Connection 으로부터 Cursor 생성
cur = conn.cursor()

# SQL 쿼리 실행
# cur.execute("select * from sqlite_master where type = 'table'; ")
 
#query =  "CREATE TABLE stocks(id INT PRIMARY KEY NOT NULL,date text NOT NULL, trans text NOT NULL, symbol text NOT NULL, qty real NOT NULL, price real NOT NULL) "

#cur.execute(query)

cur.execute("delete from leagueTable;")


cnt = 0
for i in position:
	cur.execute(("INSERT INTO leagueTable VALUES ("
		+position[cnt]+",'EPL','"+clubKor[cnt]+"',' ',"+played[cnt]+","+win[cnt]+","
		+draw[cnt]+","+lose[cnt]+",0,0,0,0)"))
	cnt+=1


# 데이타 Fetch

cur.execute("select * from leagueTable;")

rows = cur.fetchall()
for row in rows:
	print("position : ",row[0])
	print("league : ",row[1])
	print("clubKor :",row[2])
	print("clubEng :",row[3])
	print("played : ",row[4])
	print("win : ",row[5])
	print("draw : ",row[6])
	print("lose : ",row[7])
	print("gf : ",row[8])
	print("ga : ",row[9])
	print("gd : ",row[10])
	print("points : ",row[11])
 
conn.commit()


# Connection 닫기
conn.close()