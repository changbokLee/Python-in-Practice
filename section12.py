# section 12-1
# 파이썬 데이터베이스 연동(sqlite))
# 테이블 생성 및 삽입

import sqlite3
import datetime

#삽입 날짜생성
now = datetime.datetime.now()
print('now:', now)

nowDatetime = now.strftime('%Y -%m-%d %H: %M: %S')

# sqlite3
print('sqlite3.version:', sqlite3.version)
print('sqlite3.sqite_version :', sqlite3.sqlite_version)
