# 딕셔너리 (hash, jason, key-value) 

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic)

dic['etc'] = 'exersice'
print(dic)

del dic['etc']
print(dic)

print(dic['name'])
print(dic.get('dname', "값이 없습니다."))