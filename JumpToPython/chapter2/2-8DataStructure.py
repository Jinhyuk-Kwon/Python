# 변수

a = 1
b = "python"
c = [1, 2, 3]

print(id(a))
print(id(b))

b = c
c[1] = 5
print(c)
print(b)

a,b = ('python', 'life')
print(a, b)

a,b = b,a 
#서로 값 치환이 가능하다
print(a, b)