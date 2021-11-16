
# DB TEAM PROJECT #2 - 5팀(김유진, 이지원)
# COVID-19 TimeInfo.py
# INSERT DATA TO TIMEINFO

import pymysql as mysqldb
import pandas as pd
import numpy as np

# connect to MySQL local
db = mysqldb.connect(
    host='localhost',
    user='root',
    passwd='####',
    db='COVID19',
    charset='utf8'
)
cursor = db.cursor(mysqldb.cursors.DictCursor)

# 테이블 추가
sql = '''CREATE TABLE IF NOT EXISTS TIMEINFO(
date date not null primary key,
test int(11) null,
negative int(11) null,
confirmed int(11) null,
released int(11) null,
deceased int(11) null
);'''
cursor.execute(sql)


# NO_ZERO_DATE 설정 해제
sql = 'SET GLOBAL sql_mode = \'\';'
cursor.execute(sql)

# COVID_info -> dataframe
COVID_info = pd.read_csv('K_COVID19.csv')
TIME_info = pd.read_csv('addtional_Timeinfo.csv')


# 파이썬의 Nan 값을 NULL로 바꿔줌.
COVID_info = COVID_info.replace(np.nan, 'NULL')

confirmed = 0
released = 0
deceased = 0


for index, row in TIME_info.iterrows():

    # 날짜별 누적 confirmed 계산
    sql = 'SELECT count(*) as confirmed FROM PATIENTINFO WHERE confirmed_date=\'%s\'' % str(row.date)
    cursor.execute(sql)
    result = cursor.fetchone()
    confirmed = confirmed + result["confirmed"]
    # print(confirmed)

    # 날짜별 누적 released 계산
    sql = 'SELECT count(*) as released FROM PATIENTINFO WHERE released_date=\'%s\'' % str(row.date)
    cursor.execute(sql)
    result = cursor.fetchone()
    released = released + result["released"]
    # print(released)

    # 날짜별 누적 deceased 계산
    sql = 'SELECT count(*) as deceased FROM PATIENTINFO WHERE deceased_date=\'%s\'' % str(row.date)
    cursor.execute(sql)
    result = cursor.fetchone()
    deceased = deceased + result["deceased"]
    # print(deceased)

    # print(confirmed, released, deceased)

    # 튜플에 데이터 저장
    tu = (str(row.date), str(row.test), str(row.negative), str(confirmed), str(released), str(deceased))
    # print(tu)


    cursor.execute("""INSERT IGNORE INTO TIMEINFO (date, test, negative, confirmed, released, deceased)
     VALUES (%s, %s, %s, %s, %s, %s)""", tu)

    print("""INSERT IGNORE INTO TIMEINFO (date, test, negative, confirmed, released, deceased)
     VALUES (%s, %s, %s, %s, %s, %s)""", tu)

db.commit()
db.close()

print("Done")
