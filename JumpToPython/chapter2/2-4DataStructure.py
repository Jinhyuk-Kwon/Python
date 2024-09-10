# 튜플 (변경되지 않는 리스트 이뮤터블)

tuple1 = (1, 3, 5, 'a', 'b')
print(type(tuple1))
print(tuple1)

a = ()
a = (4, 6, 7)
b = (1, 2, 3)
c = ('Life', 'is', 'too', 'short')
d = (1, 2, 'Life', 'is')
e = (1, 2, ['Life', 'is'])

print(type(a))
print(e[-1][0])
#리스트와 문자열은 표현방식이 유사하다. 다만 숫자로 할 수 있는 것이 리스트이다.a

print(len(b))
print(b*3)

print(a+b)
