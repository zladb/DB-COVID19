import pymysql as mysqldb
import re
import numpy as np
import pandas as pd

# connect to MySQL server
mydb = mysqldb.connect(
    host='localhost',
    user='root',
    passwd='####',
    db='lecdb',
    charset='utf8')
cursor = mydb.cursor()

rawData = pd.read_csv("K_COVID19.csv")

#rawData.info()
needData = rawData.loc[:,['region_code','province','city','latitude.1','longitude.1','elementary_school_count',
                         'kindergarten_count', 'university_count', 'academy_ratio', 'elderly_population_ratio',
                         'elderly_alone_ratio', 'nursing_home_count']]

#print(regData.iloc[0]['region_code'])
#print(len(regData)) #5162
# 결측치행 삭제
regData = needData.dropna(subset=['region_code'])

for i in range(0,len(regData)):
    # insert R
    send = "%d , %s , %s, %f, %f, %d , %d , %d, %f, %f, %f , %d" % \
           (regData.iloc[i]['region_code'],'"{}"'.format(regData.iloc[i]['province']), '"{}"'.format(regData.iloc[i]['city']),
            regData.iloc[i]['latitude.1'], regData.iloc[i]['longitude.1'], regData.iloc[i]['elementary_school_count'],
            regData.iloc[i]['kindergarten_count'], regData.iloc[i]['university_count'], regData.iloc[i]['academy_ratio'],
            regData.iloc[i]['elderly_population_ratio'], regData.iloc[i]['elderly_alone_ratio'],  regData.iloc[i]['nursing_home_count'])

    # ROLES TABLES
    sendSql = 'INSERT INTO REGION VALUES (%s)' % (send)
    print(sendSql)

    try:
        cursor.execute(sendSql)

    except mysqldb.IntegrityError:
        print("%s already in REGION" % (regData.iloc[i]['region_code']))

# 데이타 Fetch 및 SQL 결과 출력
sql = 'Select * from REGION'
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except mysqldb.IntegrityError:
    print("cannot fetch from in REGION")

mydb.commit()
# Connection 닫기
mydb.close()

