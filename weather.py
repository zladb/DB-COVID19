import pymysql as mysqldb
import re
import numpy as np
import pandas as pd

# connect to MySQL server
mydb = mysqldb.connect(
    host='localhost',
    user='root',
    passwd='Queenmary12!',
    db='lecdb',
    charset='utf8')
cursor = mydb.cursor()

rawData = pd.read_csv("K_COVID19.csv")

needData = rawData.loc[:,['region_code','province','confirmed_date','avg_temp','min_temp','max_temp']]

# 결측치행 삭제
weaData = needData.dropna(subset=['region_code','confirmed_date'])

for i in range(0,len(weaData)):
    # insert R
    send = "%d , %s , %s, %f, %f, %f" % \
           (weaData.iloc[i]['region_code'],'"{}"'.format(weaData.iloc[i]['province']), weaData.iloc[i]['confirmed_date'],
            weaData.iloc[i]['avg_temp'], weaData.iloc[i]['min_temp'], weaData.iloc[i]['max_temp'])

    # ROLES TABLES
    sendSql = 'INSERT INTO WEATHER VALUES (%s)' % (send)
    print(sendSql)

    try:
        cursor.execute(sendSql)

    except mysqldb.IntegrityError:
        print("%s already in WEATHER" % (weaData.iloc[i]['region_code']))

# 데이타 Fetch 및 SQL 결과 출력
sql = 'Select * from WEATHER'
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except mysqldb.IntegrityError:
    print("cannot fetch from in WEATHER")

mydb.commit()
# Connection 닫기
mydb.close()





