
# COVID-19
# insert hospital data to database

import pymysql as mysqldb
import pandas as pd
import seaborn as sns
sns.set()

# connect to MySQL local
db = mysqldb.connect(
    host='localhost',
    user='root',
    passwd='a642642',
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

db.commit()
db.close()

print("Done")
