# 조건문

money = 3

if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    
#indent caution

money = 2000
card = True

if money >= 3000 or card is True:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    
a = 1 in [1, 2, 3]
print(a)
a = 1 not in [1, 2, 3]
print(a)

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
    pass # 아무것도 하지 않고 넘어가도록 하는 것
else:
    print("걸어가라")
    
    
pocket = ['paper', 'cellphone', 'card']
if 'money' in pocket:
    print("택시를 타고 가라")
elif 'card' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    

print('success') if 'money' in pocket else print('fail')