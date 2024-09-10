#exception

#f = open("나없는파일", 'r')

try:
    a = [1,2]
    #print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
    
    
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
        

try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

class Bird:
    def fly(self):
        #강제 Exception 발생
        raise NotImplementedError
        
    
class Eagle(Bird):
    #pass
    #강제로 함수를 만들어 오버라이딩 하게 
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


class MyError(Exception):
    def __str__(self):
        return "!!허용되지 않는 별명입니다.!!"
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
    
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print("허용되지 않는 별명입니다.")
    print(e)