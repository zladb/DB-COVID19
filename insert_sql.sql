
# PATIENTINFO
CREATE TABLE IF NOT EXISTS PATIENTINFO(
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
   );

# REGION
CREATE TABLE IF NOT EXISTS REGION(
   region_code INT NOT NULL,
   province VARCHAR(50) NULL,
   city VARCHAR(15) NULL,
   latitude FLOAT NULL,
   longitude FLOAT NULL,
   elementary_school_count INT NULL,
   kindergarten_count INT NULL,
   universtiy_count INT NULL,
   academy_ratio FLOAT NULL,
   elderly_population_ratio FLOAT NULL,
   elderly_alone_ratio FLOAT NULL,
   nursing_home_count INT NULL,
   PRIMARY KEY (region_code)
   );
   
# CASE   
CREATE TABLE IF NOT EXISTS CASES(
   case_id int not null primary key,
   province varchar(50) null,
   city varchar(50) null,
   infection_group tinyint(1) null,
   infection_case varchar(50) null UNIQUE,
   confirmed int null,
   latitude float null,
   longitude float null
   );

# WATHER
CREATE TABLE IF NOT EXISTS WEATHER(
   region_code INT NOT NULL,
   province VARCHAR(50),
   wdate DATE NOT NULL,
   avg_temp FLOAT NULL,
   min_temp FLOAT NULL,
   max_temp FLOAT NULL,
   PRIMARY KEY (region_code, wdate)
   );
   
# TIMEINFO   
CREATE TABLE IF NOT EXISTS TIMEINFO(
   date date not null primary key,
   test int(11) null,
   negative int(11) null,
   confirmed int(11) null,
   released int(11) null,
   deceased int(11) null
   );
   
# TIMEAGE
CREATE TABLE IF NOT EXISTS TIMEAGE(
   date date not null,
   age varchar(10) not null UNIQUE,
   confirmed int(11) null,
   deceased int(11) null,
   PRIMARY KEY(date, age)
   );
   
# TIMEGENDER   
CREATE TABLE IF NOT EXISTS TIMEGENDER(
   date DATE NOT NULL,
   sex VARCHAR(10) NOT NULL UNIQUE,
   confimed INT(11) NULL,
   released INT(11) NULL,
   deceased INT(11) NULL,
   PRIMARY KEY (date, sex)
);

# TIMEPROVINCE
CREATE TABLE IF NOT EXISTS TIMEPROVINCE(
   date DATE NOT NULL,
   province VARCHAR(50) NOT NULL UNIQUE,
   confimed INT(11) NULL,
   released INT(11) NULL,
   deceased INT(11) NULL,
   PRIMARY KEY (date, province)
);


# PATIENTINFO FK 추가 (10개)
ALTER TABLE PATIENTINFO ADD FOREIGN KEY (infection_case) REFERENCES CASES (infection_case)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE PATIENTINFO ADD FOREIGN KEY (province) REFERENCES REGION (province)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE PATIENTINFO ADD FOREIGN KEY (confirmed_date) REFERENCES WEATHER (wdate)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE PATIENTINFO ADD FOREIGN KEY (age) REFERENCES TIMEAGE (age);

ALTER TABLE PATIENTINFO ADD FOREIGN KEY (sex) REFERENCES TIMEGENDER (sex);

ALTER TABLE PATIENTINFO ADD FOREIGN KEY (province) REFERENCES TIMEPROVINCE (province);

ALTER TABLE PATIENTINFO ADD FOREIGN KEY (confirmed_date) REFERENCES TIMEINFO (date)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE PATIENTINFO ADD FOREIGN KEY (released_date) REFERENCES TIMEINFO (date)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE PATIENTINFO ADD FOREIGN KEY (deceased_date) REFERENCES TIMEINFO (date)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE PATIENTINFO ADD FOREIGN KEY (infected_by) REFERENCES PATIENTINFO (patient_id)
ON DELETE SET NULL ON UPDATE CASCADE;


# TIMEAGE FK 추가
ALTER TABLE TIMEAGE ADD FOREIGN KEY (date) REFERENCES TIMEINFO (date);

# TIMEGENDER FK 추가
ALTER TABLE TIMEGENDER ADD FOREIGN KEY (date) REFERENCES TIMEINFO (date);

# TIMEPROVINCE FK 추가
ALTER TABLE TIMEPROVINCE ADD FOREIGN KEY (date) REFERENCES TIMEINFO (date);

# 제약 조건 이름 바꾸는건 어떻게 할까???

