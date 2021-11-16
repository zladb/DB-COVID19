
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
   infection_case varchar(50) null,
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
   age varchar(10) not null,
   confirmed int(11) null,
   deceased int(11) null,
   PRIMARY KEY(date, age)
   );
   
# TIMEGENDER   
CREATE TABLE IF NOT EXISTS TIMEGENDER(
   date DATE NOT NULL,
   sex VARCHAR(10) NOT NULL,
   confimed INT(11) NULL,
   released INT(11) NULL,
   deceased INT(11) NULL,
   PRIMARY KEY (date, sex)
);

# TIMEPROVINCE
CREATE TABLE IF NOT EXISTS TIMEPROVINCE(
   date DATE NOT NULL,
   province VARCHAR(50) NOT NULL,
   confimed INT(11) NULL,
   released INT(11) NULL,
   deceased INT(11) NULL,
   PRIMARY KEY (date, province)
);
