# 변수 선언 및 할당
name = "Alice"
age = 25
height = 5.6

# 데이터 타입 확인
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(height))  # <class 'float'>


age = 20

if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")
    
    # for 반복문
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# while 반복문
count = 0
while count < 5:
    print(count)
    count += 1
    
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple

# 리스트에 항목 추가
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']