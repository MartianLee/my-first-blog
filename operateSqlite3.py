import sqlite3

# SQLite DB 연결
conn = sqlite3.connect("db.sqlite3")
 
# Connection 으로부터 Cursor 생성
cur = conn.cursor()
 
# SQL 쿼리 실행
# cur.execute("select * from sqlite_master where type = 'table'; ")
#cur.execute("select * from blog_post; ")
 
#query =  "CREATE TABLE stocks(id INT PRIMARY KEY NOT NULL,date text NOT NULL, trans text NOT NULL, symbol text NOT NULL, qty real NOT NULL, price real NOT NULL) "
query =  ("CREATE TABLE leagueTable("
+ "position INT NOT NULL,"
+ "league TEXT NOT NULL,"
+ "clubKor TEXT NOT NULL,"
+ "clubEng TEXT NOT NULL,"
+ "played INT NOT NULL,"
+ "win INT NOT NULL,"
+ "draw INT NOT NULL, "
+ "lose INT NOT NULL, "
+ "gf INT NOT NULL, "
+ "ga INT NOT NULL, "
+ "gd INT NOT NULL, "
+ "points INT NOT NULL,"
+ "PRIMARY KEY (position,league) )"
)

#cur.execute(query)

#cur.execute("DROP TABLE stocks");

#cur.execute("INSERT INTO stocks VALUES ('2','2016-10-12','SELL','RHAT',300,25.14)")

cur.execute("select * from leagueTable;")

# 데이타 Fetch
rows = cur.fetchall()
for row in rows:
	print("position : ",row[0])
	print("league : ",row[1])
	print("clubKor :",row[2])
	print("played : ",row[3])
	print("win : ",row[4])
	print("draw : ",row[5])
	print("lose : ",row[6])
	print("gf : ",row[7])
	print("ga : ",row[8])
	print("gd : ",row[9])
	print("points : ",row[10])
	
 
conn.commit()

# Connection 닫기
conn.close()