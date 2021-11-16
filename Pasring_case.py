
# DB TEAM PROJECT #2 - 5팀(김유진, 이지원)
# COVID-19 Pasring_case.py
# add case to database

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
cursor = db.cursor()

# 테이블 추가
sql = '''CREATE TABLE IF NOT EXISTS CASES(
case_id int not null primary key,
province varchar(50) null,
city varchar(50) null,
infection_group tinyint(1) null,
infection_case varchar(50) null,
confirmed int null,
latitude float null,
longitude float null);'''
cursor.execute(sql)


# NO_ZERO_DATE 설정 해제
sql = 'SET GLOBAL sql_mode = \'\';'
cursor.execute(sql)

# COVID_info -> dataframe
COVID_info = pd.read_csv('K_COVID19.csv')


# 중복되는 컬럼(city, latitude, longitude)의 이름을 다르게 설정해줌.
COVID_info.columns = ['patient_id', 'sex', 'age', 'country', 'province', 'p-city', 'infection_case', 'infected_by',
                      'contact_number', 'symptom_onset_date', 'confirmed_date', 'released_date', 'deceased_date',
                      'state', 'avg_temp', 'min_temp', 'max_temp', 'case_id', 'c_city', 'infection_group', 'confirmed',
                      'c_latitude', 'c_longitude', 'region_code', 'r_latitude', 'r_longitude',
                      'elementary_school_count', 'kindergarten_count', 'university_count', 'academy_ratio',
                      'elderly_population_ratio', 'elderly_alone_ratio', 'nursing_home_count']

# 파이썬의 Nan 값을 NULL로 바꿔줌.
COVID_info = COVID_info.replace(np.nan, 'NULL')

for index, row in COVID_info.iterrows():

    # 튜플에 데이터 저장
    tu = (str(row.case_id), row.province, row.c_city, str(row.infection_group), row.infection_case, str(row.confirmed),
          str(row.c_latitude), str(row.c_longitude))
    # print(tu)

    cursor.execute("""INSERT IGNORE INTO CASES (case_id, province, city, infection_group, infection_case, confirmed, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""", tu)

    print("""INSERT IGNORE INTO CASES (case_id, province, city, infection_group, infection_case, confirmed, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""", tu)

# case_id = null인 case 삭제
cursor.execute("DELETE FROM CASES WHERE case_id=\'0\';")
db.commit()
db.close()

print("Done")
