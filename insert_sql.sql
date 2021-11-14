
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


CREATE TABLE REGION(
   region_code INT NOT NULL,
   province VARCHAR(50),
   city VARCHAR(15),
   latitude FLOAT,
   longitude FLOAT,
   elementary_school_count INT,
   kindergarten_count INT,
   universtiy_count INT,
   academy_ratio FLOAT,
   elderly_population_ratio FLOAT,
   elderly_alone_ratio FLOAT,
   nursing_home_count INT,
   PRIMARY KEY (region_code)
   );
   
   
CREATE TABLE IF NOT EXISTS CASES(
   case_id int not null primary key,
   province varchar(50) null,
   city varchar(50) null,
   infection_group tinyint(1) null,
   infection_case varchar(50) null,
   confirmed int null,
   latitude float null,
   longitude float null
   );


CREATE TABLE WEATHER(
   region_code INT NOT NULL,
   province VARCHAR(50),
   wdate DATE NOT NULL,
   avg_temp FLOAT,
   min_temp FLOAT,
   max_temp FLOAT,
   PRIMARY KEY (region_code, wdate)
   );
   
   
CREATE TABLE IF NOT EXISTS TIMEINFO(
   date date not null primary key,
   test int(11) null,
   negative int(11) null,
   confirmed int(11) null,
   released int(11) null,
   deceased int(11) null
   );
   
CREATE TABLE TimeGender(
   date DATE NOT NULL,
   sex VARCHAR(10) NOT NULL,
   confimed INT(11),
   released INT(11),
   deceased INT(11),
   PRIMARY KEY (date, sex)
);
