
# COVID-19
# add timeage to database

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
sql = '''CREATE TABLE IF NOT EXISTS TIMEAGE(
date date not null,
age varchar(10) not null,
confirmed int(11) null,
deceased int(11) null,
PRIMARY KEY(date, age)
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

confirmed_count = {'0s': 0, '10s': 0, '20s': 0, '30s': 0, '40s': 0, '50s': 0, '60s': 0, '70s': 0, '80s': 0, '90s': 0, '100s': 0, 'NULL': 0}
deceased_count = {'0s': 0, '10s': 0, '20s': 0, '30s': 0, '40s': 0, '50s': 0, '60s': 0, '70s': 0, '80s': 0, '90s': 0, '100s': 0, 'NULL': 0}


# 1. 먼저 confirmed 데이터 먼저 삽입.
for index, row in TIME_info.iterrows():

    # 날짜/나이 별 확진 수
    sql = 'SELECT age, confirmed_date, count(*) as c_count FROM PATIENTINFO WHERE confirmed_date=\'%s\' GROUP BY (age)' % str(row.date)
    cursor.execute(sql)
    result1 = cursor.fetchall()
    # print(list(result1))

    c_len = len(result1)
    if c_len > 0:
        for c in result1:
            temp = confirmed_count['%s' % c['age']] + c['c_count']
            confirmed_count.update({('%s' % c['age']): temp})
            # print(confirmed_count)


    sql = 'SELECT age, deceased_date, count(*) as d_count FROM PATIENTINFO WHERE deceased_date=\'%s\' GROUP BY (age)' % str(row.date)
    cursor.execute(sql)
    result2 = cursor.fetchall()
    # print(result2)

    d_len = len(result2)
    if d_len > 0:
        for d in result2:
            temp = deceased_count['%s' % d['age']] + d['d_count']
            deceased_count.update({('%s' % d['age']): temp})
            # print(deceased_count)

    # 데이터 삽입하기
    for age in confirmed_count.keys():
        tu = (str(row.date), str(age), str(confirmed_count['%s' % age]), str(deceased_count['%s' % age]))
        # print(tu)

        cursor.execute("""INSERT IGNORE INTO TIMEAGE (date, age, confirmed, deceased) VALUES (%s, %s, %s, %s)""", tu)
        print("""INSERT IGNORE INTO TIMEAGE (date, age, confirmed, deceased) VALUES (%s, %s, %s, %s)""", tu)


# age가 null인 데이터 삭제
cursor.execute("DELETE FROM TIMEAGE WHERE age=\'NULL\';")

db.commit()
db.close()

print("Done")
