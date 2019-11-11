# CSV: MIME - text/csv

import csv
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)

    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter ='|')

    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


# 예제 3(Dict 변환)

with open('./resource/sample1.csv', 'r')as f:
    reader =csv.DictReader(f)

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('________________________')


# 예제4
w = [[1,2,3], [4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv', 'w', newline= '') as f:
    wt =csv.writer(f)

    for v in w:
        wt.writerow(v)

#예제 5
with open('./resource/sample4.csv', 'w', newline= '')as f:
    wt = csv.writer(f)
    wt.writerows(w)


#XSL ,XLSX
#openpyxl, xlsxwriter , xlrd ,xlwt ,xlutils
#pandas를 주로 사용(openpyxl, xlrd)
# pip install

import pandas as pd

xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위데이터 확인
print(xlsx.head())
print()

#데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) # 행,  열

# 엑셀 or csv 다시쓰기
xlsx.to_excel('./resource/result.xlsx', index = False)
xlsx.to_csv('./resource/result.csv', index = False)

