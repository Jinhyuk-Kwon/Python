# 타입이 바뀌어도 문제가 되지 않는 동적 언어이다.
a = 1
print(type(a))

a = "1"
print(type(a))

num: int = 1
#num은 힌트만 제공한다. 만약 제약을 두고 싶다면 mypy를 install 해서 사용한다.
num = "time"

