#section 09
# 파일 읽기, 쓰기
# 읽기 모드 : r , 쓰기모드 : w, 추가모드 : a
#..상대경로 . 절대경로

f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
# print(dir(f))
#반드시 close 리소스 반환
f.close()

print("----------------------------------")
print("----------------------------------")

with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))
print()


with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())
print("----------------------------------")
print("----------------------------------")


with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content)

print("----------------------------")
print("----------------------------")


# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
  #  print(line)
    while line:
        print(line, end = '######')
        line = f.readline()

