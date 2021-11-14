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

CovData = covData.loc[:,['sex', 'confirmed_date','released_date','deceased_date']]
TimeData = TimeData.loc[:,['date']]

# 결측치행 삭제
CovData = CovData.dropna(subset=['sex', 'confirmed_date'])
TimeData = TimeData.dropna(subset=['date'])

# timedata날짜별로 읽어가면서
# 남/녀의 각각 확진자, released, deceased 순서대로 누적해가기
mCon, fCon, mRel, fRel, mDec, fDec = 0, 0, 0, 0, 0, 0

for i in range(0, len(TimeData)):
    # 확진 날짜만 분리
    conDate = CovData[TimeData.iloc[i]['date'] == CovData['confirmed_date']]
    mCon += len(conDate[conDate['sex'] == 'male'])
    fCon += len(conDate[conDate['sex'] == 'female'])
    # 해제 날짜 분리
    relDate = CovData[TimeData.iloc[i]['date'] == CovData['released_date']]
    mRel += len(relDate[relDate['sex'] == 'male'])
    fRel += len(relDate[relDate['sex'] == 'female'])
    # 사망 날짜 분리
    decDate = CovData[TimeData.iloc[i]['date'] == CovData['deceased_date']]
    mDec += len(decDate[decDate['sex'] == 'male'])
    fDec += len(decDate[decDate['sex'] == 'female'])

    # 입력값 순서대로 날짜, 성별, confirmed released deceased
    male = "%s , %s , %s, %s, %s" % \
           ('"{}"'.format(TimeData.iloc[i]['date']), '"{}"'.format("male"), mCon, mRel, mDec)
    female = "%s , %s , %s, %s, %s" % \
             ('"{}"'.format(TimeData.iloc[i]['date']), '"{}"'.format("female"), fCon, fRel, fDec)

    mSql = 'INSERT INTO TimeGender VALUES (%s)' % (male)
    fSql = 'INSERT INTO TimeGender VALUES (%s)' % (female)
    # male
    print(mSql)
    try:
        cursor.execute(mSql)
    except mysqldb.IntegrityError:
        print("male %s already in TimeGender" % (conDate.iloc[i]['date']))

    # female
    try:
        cursor.execute(fSql)
    except mysqldb.IntegrityError:
        print("female %s already in TimeGender" % (conDate.iloc[i]['date']))

# 데이타 Fetch 및 SQL 결과 출력
sql = 'Select * from TimeGender'
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except mysqldb.IntegrityError:
    print("cannot fetch from in TimeGender")

covidDb.commit()
# Connection 닫기
covidDb.close()





