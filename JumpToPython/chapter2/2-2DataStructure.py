# 문자형
a="Life is too short, You need Python"
b="a"
c="123"
print('='*50)
print(a+b+c)
print(a*2)
print('='*50)
print(len(a))
print(a[3])
print(a[4:])
print(a[4::2])
print(a[4::-1])
print(a[7:19:-1])

a="I eat %d apples" %5
print(a)
a="I eat %s apples" %"five"
print(a)
a="%10s" % "hi"
print(a)
a="%-10s" % "hi"
print(a)
a="%0.4f" % 3.42134531
print(a)
a="I eat {} apples".format(5)
print(a)
a="I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(a)
name = '홍길동'
age = 30
a=f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.'
print(a)

a = "hobby"
print(a.count('b'))
print(a.find('b'))
print(a.find('x'))
print(a.index('b'))

a=",".join('abcd')
print(a)
a=",".join(['a', 'b', 'c', 'd'])
print(a)
