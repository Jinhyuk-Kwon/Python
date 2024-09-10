# 반복문 for


test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)
    
a = [(1,2), (3,4), (5,6)]
for first, last in a:
    print(first + last)
    
    
marks = [90, 25, 67, 45, 80]
number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number += 1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)
        
        
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)
    
add = 0
for i in range(1,10):
    add += i
    print(add)
    
    
for i in range(3,8):
    for j in range(1,10):
        print(i*j, end=" ")   #엔터가 아닌 end를 띄어쓰기로 변경.
    print("")

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
#result = [num * 3 for num in a]
#result = [num * 3 for num in a if num%2 == 0]
print(result)
