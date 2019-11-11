# 클래스 책읽는 사람: book reader
# 속성: 이름 -> name
# 메소드 : 책읽기 -> read_book
# 클래스작성법은 낙타표기법을 따르고있다. 대문자가 왓다갓다하는게 낙타같아서
class BookReader:
    name = str()
    def read_book(self): # 파이썬내에서는 자동으로 인자값이 존재한다 바로 self 본인의 객체를 인자값으로 넘김으로 써 함수내에서 클래스의 속성및 메소드를 접근
        print (self.name + 'is readingBook!')


