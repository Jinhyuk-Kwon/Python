# 반복문

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
        
#파이썬은 treeHit++ 이 문법이 안됨 ㅠ += 을 사용해야 한다.


prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())
    
print('\n')
    
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)