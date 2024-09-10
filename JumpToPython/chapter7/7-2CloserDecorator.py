# closure.py
import time

class Mul:
    def __init__(self, m):
        self.m = m

    def __call__(self, n):    #인스턴스에서 함수 이름 없이 수행가능한 함수
        return self.m * n

    def mul(self, n):
        return self.m * n

#클로저는 간단히 말해 함수 안에 내부 함수(inner function)를 구현하고 그 내부 함수를 리턴하는 함수를 말한다. 
#이때 외부 함수는 자신이 가진 변숫값 등을 내부 함수에 전달할 수 있다.
def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

    
def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

@elapsed   #데코레이터 함수 꾸미는 기능 
def myfunc():
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print("함수 수행시간: %f 초" % (end-start))

if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10))  # 30 출력
    print(mul5(10))  # 50 출력
    
    print(mul3.mul(10))  # 30 출력
    print(mul5.mul(10))  # 50 출력
    
    mul7 = mul(7)

    print(mul7(10))  # 70 출력
    myfunc()
    #decorated_myfunc = elapsed(myfunc)
    #decorated_myfunc()