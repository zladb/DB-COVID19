
# COVID-19
# insert hospital data to database

import pymysql as mysqldb
import pandas as pd
import seaborn as sns
from math import dist
sns.set()

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
sql = '''CREATE TABLE IF NOT EXISTS HOSPITAL(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    province VARCHAR(50) NULL,
    city VARCHAR(15) NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    capacity INT NOT NULL,
    current INT NULL
);'''
cursor.execute(sql)

# patientinfo에 hospital_id column을 추가한다. 만약 존재한다면 이 부분을 주석처리해준다.
sql = 'ALTER TABLE PATIENTINFO ADD hospital_id INT NULL;'
cursor.execute(sql)

# hospital_info -> dataframe
hospital_info = pd.read_csv('Hospital.csv')
hospital_info.columns = ['id', 'h_name', 'province', 'city', 'latitude', 'longitude', 'capacity', 'current']

for index, row in hospital_info.iterrows():

    # 튜플에 데이터 저장
    tu = (str(row.id), str(row.h_name), row.province, row.city, str(row.latitude), str(row.longitude), str(row.capacity), str(row.current))
    print(tu)

    cursor.execute("""INSERT IGNORE INTO HOSPITAL (id, name, province, city, latitude, longitude, capacity, current)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", tu)

    print("""INSERT IGNORE INTO HOSPITAL (hospital_id, hospital_name, hospital_province, hospital_city, hospital_latitude,
    hospital_longitude, capacity, current) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", tu)

# region_info -> dataframe
region_info = pd.read_csv('Region.csv')

for index, row in region_info.iterrows():

    # 튜플에 데이터 저장
    tu = (str(row.code), row.province, row.city, str(row.latitude), str(row.longitude), str(row.elementary_school_count),
          str(row.kindergarten_count), str(row.university_count), str(row.academy_ratio),
          str(row.elderly_population_ratio), str(row.elderly_alone_ratio), str(row.nursing_home_count))
    print(tu)

    # region table에 없는 data 보충
    cursor.execute("""INSERT IGNORE INTO REGION (region_code, province, city, latitude, longitude,
    elementary_school_count, kindergarten_count, universtiy_count, academy_ratio, elderly_population_ratio,
    elderly_alone_ratio, nursing_home_count)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tu)

    print("""INSERT IGNORE INTO REGION (region_code, province, city, latitude, longitude,
    elementary_school_count, kindergarten_count, universtiy_count, academy_ratio, elderly_population_ratio,
    elderly_alone_ratio, nursing_home_count)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tu)

db.commit()

# 모든 환자의 경도와 위도 값을 받아온다.
sql = '''SELECT p.patient_id, p.province, p.city, r.latitude, r.longitude
FROM REGION r, PATIENTINFO p
WHERE r.province = p.province and r.city = CASE WHEN p.city='etc' then p.province ELSE p.city END'''
cursor.execute(sql)
PatientList = cursor.fetchall()

for patient in PatientList:
    print(patient)

    # 모든 병원의 정보를 받아온다.
    sql = 'SELECT * from hospital'
    cursor.execute(sql)
    HospitalList = cursor.fetchall()
    # print(HospitalList)

    closest = 100000
    x = (patient[3], patient[4])
    for hospital in HospitalList:
        y = (hospital[4], hospital[5])

        # capacity > current : 환자를 수용할 수 있는 병원 중 가장 가까운 곳을 찾는다.
        if hospital[6] > hospital[7]:
            distance = dist(x, y)
            if distance < closest:
                closest = distance
                close_hospital = hospital

    print(closest)
    print(close_hospital)

    # 환자가 입원하고 있는 병원정보 업데이트
    sql = '''update patientinfo set hospital_id = {0} where patient_id = {1}'''.format(close_hospital[0], patient[0])
    cursor.execute(sql)

    # 병원의 현재 수용인원 업데이트
    sql = '''update hospital set current = current + 1 where id = {0}'''.format(close_hospital[0])
    cursor.execute(sql)

db.commit()
db.close()

print("Done")
