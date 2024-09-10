# 함수의 구조

def funtion_name(parameter1):
    print(f'parameter1={parameter1}')
    
funtion_name(4)

def add(a, b): 
    return a + b

print(add(2,3))

def say(): 
    return 'Hi' 
a = say()
print(a)


def add(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
    
a = add(2,3)
print(a)

def sub(a,b):
    return a-b

a = sub(b=3, a=1)
print(a)

def add_many(*args): 
    result = 0 
    for i in args: 
        result = result + i   # *args에 입력받은 모든 값을 더한다.
    return result 

print(add_many(2,4,6,8,2,3,4,5,7,3,27364))

def add_mul(choice, *args): 
    if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
        result = 1 
        for i in args: 
            result = result * i 
    return result 

print(add_mul("add", 1,2,3,4,5))
print(add_mul("mul", 1,2,3,4,5))

#dictionary 형태로 인자를 받음.
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name='foo', age=3)
print_kwargs(a=1, b=3)


def add_and_mul(a,b): 
    return a+b, a*b
result = add_and_mul(3,4)
print(result)

def say_nick(nick): 
    if nick == "바보": 
        return 
    print("나의 별명은 %s 입니다." % nick)
    
nickname = '바보1'
say_nick(nickname)

#초기값이 있는 파라메터는 뒷쪽에만 둔다.

a = 1  #전역변수
def vartest(a):
    a = a + 1    #지역변수
vartest(a)
print(a)

a = 1  #전역변수
def vartest(a):
    return a + 1    #지역변수
a = vartest(a)
print(a)

a = 1  #전역변수
def vartest():
    global a    #전역변수
    a += 1
vartest()
print(a)

# 리스트, 딕셔너리, set은 변형가능하므로 주소값이 전달되어 함수내에서 바로 변경이 가능하다.
b = [1,2,3]
def vartest2(b):
    b.append(4)
vartest2(b)
print(b)

def add(a, b):
    return a + b
result = add(3, 4)
print(result)