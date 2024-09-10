# 유저 입출력 

number = input("숫자를 입력하세요: ")    #input은 모든 입력을 string으로 취급
print(number)

#큰 따옴표로 구분되는 것은 +와 동일한 기능
print("life" "is" "too short")  # 1번
print("life"+"is"+"too short")  # 2번

#문자열 띄어쓰기는 쉼표로 혹은 그냥 스페이스 넣기
print("life", "is", "too short")

for i in range(10):
    print(i, end=' ')
    
print("what?")

