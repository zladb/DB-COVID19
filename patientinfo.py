
# COVID-19
# add patientinfo to database

import pymysql as mysqldb
import pandas as pd
import numpy as np
import seaborn as sns
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
sql = '''CREATE TABLE IF NOT EXISTS PATIENTINFO(
patient_id bigint not null primary key,
sex varchar(10) null,
age varchar(10) null,
country varchar(50) null,
province varchar(50) null,
city varchar(50) null,
infection_case varchar(50) null,
infected_by bigint null,
contact_number int null,
symptom_onset_date date null,
confirmed_date date null,
released_date date null,
deceased_date date null,
state varchar(20) null
)'''
cursor.execute(sql)


# NO_ZERO_DATE 설정 해제
sql = 'SET GLOBAL sql_mode = \'\';'
cursor.execute(sql)

# COVID_info -> dataframe
COVID_info = pd.read_csv('K_COVID19.csv')

# 파이썬의 Nan 값을 NULL로 바꿔줌.
COVID_info = COVID_info.replace(np.nan, 'NULL')

for index, row in COVID_info.iterrows():

    # 튜플에 데이터 저장
    tu = (str(row.patient_id), row.sex, row.age, row.country, row.province, row.city, row.infection_case,
          str(row.infected_by), str(row.contact_number), row.symptom_onset_date, row.confirmed_date, row.released_date,
          row.deceased_date, row.state)
    # print(tu)

    cursor.execute("""INSERT IGNORE INTO PATIENTINFO (patient_id, sex, age, country, province, city,
    infection_case, infected_by, contact_number, symptom_onset_date, confirmed_date, released_date,
    deceased_date, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tu)

    print("""INSERT IGNORE INTO PATIENTINFO (patient_id, sex, age, country, province, city,
    infection_case, infected_by, contact_number, symptom_onset_date, confirmed_date, released_date,
    deceased_date, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tu)


sql = 'SET foreign_key_checks = 0;'
cursor.execute(sql)

# ADD foreign key
sql = 'ALTER TABLE PATIENTINFO ADD FOREIGN KEY (infected_by) REFERENCES PATIENTINFO (patient_id) ' \
      'ON DELETE SET NULL ON UPDATE CASCADE;'
cursor.execute(sql)

# ADD foreign key
sql = 'ALTER TABLE PATIENTINFO ADD FOREIGN KEY (infection_case) REFERENCES CASE (infection_case) ' \
      'ON DELETE SET NULL ON UPDATE CASCADE;'
cursor.execute(sql)

# ADD FK CONSTRAINT
# sql = 'ALTER TABLE PATIENTINFO ADD CONSTRAINT \'fk_infected_by_patientinfo_patient_id\'' \
#       'FOREIGN KEY (infected_by) REFERENCES PATIENTINFO (patient_id) ' \
#       'ON DELETE SET NULL ON UPDATE CASCADE;'
# cursor.execute(sql)

# ADD FK CONSTRAINT
# sql = 'ALTER TABLE PATIENTINFO ADD CONSTRAINT \'fk_infection_case_case_infection_case\'' \
#       'FOREIGN KEY (infection_case) REFERENCES CASE (infection_case) ' \
#       'ON DELETE SET NULL ON UPDATE CASCADE;'
# cursor.execute(sql)

sql = 'SET foreign_key_checks = 1;'
cursor.execute(sql)

db.commit()
db.close()

print("Done")
