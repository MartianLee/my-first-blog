# -*- coding: utf-8 -*-

import urllib.request
import os, csv
import sqlite3
import json
import re
from bs4 import BeautifulSoup
#from urllib.request import urlopen


# SQLite DB 연결
conn = sqlite3.connect("db.sqlite3")

# Connection 으로부터 Cursor 생성
cur = conn.cursor()

# SQL 쿼리 실행
# cur.execute("select * from sqlite_master where type = 'table'; ")
#query =  "CREATE TABLE stocks(id INT PRIMARY KEY NOT NULL,date text NOT NULL, trans text NOT NULL, symbol text NOT NULL, qty real NOT NULL, price real NOT NULL) "
#cur.execute(query)
#cur.execute("delete from leagueTable;")

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

#conn.commit()


# Connection 닫기
conn.close()
