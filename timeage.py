
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


# 1. 먼저 confirmed 데이터 먼저 삽입.
for index, row in TIME_info.iterrows():

    # 날짜/나이 별 확진 수
    sql = 'SELECT age, confirmed_date, count(*) as c_count FROM PATIENTINFO WHERE confirmed_date=\'%s\' GROUP BY (age)' % str(row.date)
    cursor.execute(sql)
    result1 = cursor.fetchall()
    c_len = len(result1)
    result1 = list(result1)
    # print(list(result1))

    if c_len > 0:
        for c in result1:
            # 튜플에 데이터 저장
            tu = (str(c['confirmed_date']), str(c['age']), str(c['c_count']), str('0'))
            # print(tu)

            cursor.execute("""INSERT IGNORE INTO TIMEAGE (date, age, confirmed, deceased) VALUES (%s, %s, %s, %s)""", tu)
            print("""INSERT IGNORE INTO TIMEAGE (date, age, confirmed, deceased) VALUES (%s, %s, %s, %s)""", tu)


# 2. deceased 데이터를 추가하는데
# 앞서 추가한 PK와 겹치면 update로 deceased 값만 넣어주고, PK가 없으면 튜플을 새로 생성해서 값을 넣는다.
for index, row in TIME_info.iterrows():

    sql = 'SELECT age, deceased_date, count(*) as d_count FROM PATIENTINFO WHERE deceased_date=\'%s\' GROUP BY (age)' % str(row.date)
    cursor.execute(sql)
    result2 = cursor.fetchall()
    d_len = len(result2)
    result2 = list(result2)
    # print(result2)

    if d_len > 0:
        for d in result2:

            # 데이터의 여부로 해당 key가 존재하는지 확인한다.
            sql = 'SELECT count(*) FROM TIMEAGE WHERE date=\'%s\' and age=\'%s\'' % (d['deceased_date'], d['age'])
            cursor.execute(sql)
            result3 = cursor.fetchall()

            for insert in result3:
                val = insert['count(*)']

                # 겹치는 key가 없으면 새로 생성해서 넣는다.
                if val == 0:
                    tu = (str(d['deceased_date']), str(d['age']), str('0'), str(d['d_count']))
                    #print(tu)

                    cursor.execute(
                        """INSERT IGNORE INTO TIMEAGE (date, age, confirmed, deceased) VALUES (%s, %s, %s, %s)""", tu)
                    print("""INSERT IGNORE INTO TIMEAGE (date, age, confirmed, deceased) VALUES (%s, %s, %s, %s)""", tu)

                # 겹치는 key가 있다면 deceased 값을 넣어준다.
                elif val == 1:
                    sql = 'UPDATE TIMEAGE SET deceased := \'%s\' WHERE date=\'%s\' and age=\'%s\'' % (d['d_count'], d['deceased_date'], d['age'])
                    cursor.execute(sql)
                    print('UPDATE TIMEAGE SET deceased := \'%s\' WHERE date=\'%s\' and age=\'%s\'' % (d['d_count'], d['deceased_date'], d['age']))


# age가 null인 데이터 삭제
cursor.execute("DELETE FROM TIMEAGE WHERE age=\'NULL\';")
db.commit()
db.close()

print("Done")
