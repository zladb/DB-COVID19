import pymysql as mysqldb
import pandas as pd

# connect to MySQL server
covidDb = mysqldb.connect(
    host='localhost',
    user='root',
    passwd='Queenmary12!',
    db='COVID19',
    charset='utf8')
cursor = covidDb.cursor()

covData = pd.read_csv("K_COVID19.csv")
TimeData = pd.read_csv("addtional_Timeinfo.csv")

CovData = covData.loc[:,['province', 'confirmed_date','released_date','deceased_date']]
TimeData = TimeData.loc[:,['date']]

# 결측치행 삭제
CovData = CovData.dropna(subset=['province', 'confirmed_date'])
CovData = CovData.sort_values(by='province')
TimeData = TimeData.dropna(subset=['date'])

# province별로 묶기 읽어가면서
provName = CovData.groupby(['province'])
#conDate = CovData.groupby(['province', 'confirmed_date'])

# 해당 지역별 날짜마다 확진, 격리해제, 사망자 수
for key, group in provName: #key에는 각 지역의 이름이 담겨있다
    con, rel, dec = 0, 0, 0
    # 지역별 정보가 담긴 dadtaframe을 생성 후 날짜 기준으로 sorting
    provDate = CovData[key == CovData['province']]
    provDate = provDate.sort_values(by='confirmed_date')
    for i in range(0, len(TimeData)):
        #print(key)
        #print("* count", len(group))
        con += len(provDate[TimeData.iloc[i]['date'] == provDate['confirmed_date']])
        rel += len(provDate[TimeData.iloc[i]['date'] == provDate['released_date']])
        dec += len(provDate[TimeData.iloc[i]['date'] == provDate['deceased_date']])

        # 입력값 순서대로 날짜, 지역, confirmed released deceased
        prov = "%s , %s , %s, %s, %s" % ('"{}"'.format(TimeData.iloc[i]['date']), '"{}"'.format(key), con, rel, dec)


        sql = 'INSERT INTO TimeProvince VALUES (%s)' % (prov)
        print(sql)

        try:
            cursor.execute(sql)
        except mysqldb.IntegrityError:
            print("%s %s already in TimeProvince" % ('"{}"'.format(TimeData.iloc[i]['date']), '"{}"'.format(key)))


# 데이타 Fetch 및 SQL 결과 출력
sql = 'Select * from TimeProvince'
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except mysqldb.IntegrityError:
    print("cannot fetch from in TimeProvince")

covidDb.commit()
# Connection 닫기
covidDb.close()
