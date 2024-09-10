# 리스트

odd = [1, 3, 5, 7, 9]
print(type(odd))
print(odd)

a = []
a = [4, 6, 7]
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print(e[-1][0])
#리스트와 문자열은 표현방식이 유사하다. 다만 숫자로 할 수 있는 것이 리스트이다.a

print(len(b))
print(b*3)

b.append(4)
print(b)
b.sort()
b.reverse()
print(b)
print(b.pop())
print(b.count(2))