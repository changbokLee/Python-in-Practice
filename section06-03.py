# 힌트
def func_mul3(x : int ) -> list:
    y1  =x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1,y2,y3]

print(func_mul3(5.0))


# 람다식예제    
# 람다식 : 메모리 절약 ,가독성향상 코드간결
# 함수는 객체생성 -> 리소스 메모리할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수할당
def mul_10(num : int)-> int:
    return num * 10
var_func =mul_10
print(var_func)
print(type(var_func))
print(var_func(10))

lambda_mul_10 =lambda x: x*10