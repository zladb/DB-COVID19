import pymysql as mysqldb
import pandas as pd

def isnan(num):
    return num != num

# connect to MySQL server
covidDb = mysqldb.connect(
    host='localhost',
    user='root',
    passwd='####',
    db='COVID19',
    charset='utf8')
cursor = covidDb.cursor()

rawData = pd.read_csv("K_COVID19.csv")
needData = rawData.loc[:,['region_code','province','confirmed_date','avg_temp','min_temp','max_temp']]

# 결측치행 삭제
weaData = needData.dropna(subset=['region_code','confirmed_date'])
for i in range(0,len(weaData)):
    wea = "%d , %s , %s, %s, %s, %s" % \
           (weaData.iloc[i]['region_code'],
            '"{}"'.format(weaData.iloc[i]['province']),
            '"{}"'.format(weaData.iloc[i]['confirmed_date']),
            "NULL" if isnan(weaData.iloc[i]['avg_temp']) else float(weaData.iloc[i]['avg_temp']),
            "NULL" if isnan(weaData.iloc[i]['avg_temp']) else float(weaData.iloc[i]['min_temp']),
            "NULL" if isnan(weaData.iloc[i]['avg_temp']) else float(weaData.iloc[i]['max_temp']))

    weaSql = 'INSERT INTO WEATHER VALUES (%s)' % (wea)
    print(weaSql)

    try:
        cursor.execute(weaSql)
    except mysqldb.IntegrityError:
        print("%s already in WEATHER" % (weaData.iloc[i]['region_code']))

# 데이타 Fetch 및 SQL 결과 출력
sql = 'Select * from WEATHER'
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except mysqldb.IntegrityError:
    print("cannot fetch from in WEATHER")

covidDb.commit()
# Connection 닫기
covidDb.close()







