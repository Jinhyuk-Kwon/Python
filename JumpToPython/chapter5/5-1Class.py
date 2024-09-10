#class 

result = 0

def add(num):
    global result
    result += num  # 결괏값(result)에 입력값(num) 더하기
    return result  # 결괏값 리턴

print(add(3))
print(add(4))



class Calculator:
    def __init__(self):      #생성자
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class cookie:
    pass

chocoCookie = cookie()
AlmondCookie = cookie()

class FourCal:
    def __init__(self):
        self.first = 0
        self.second = 0
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
        
calc1=FourCal()
calc1.setdata(2,4)        
print(calc1.first, calc1.second)
print(calc1.add())


class MoreFourcal(FourCal):
    def power(self):
        result = self.first ** self.second
        return result
    
a = MoreFourcal()
a.setdata(2,5)
print(a.add())


class SafeFourcal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result
    
    

b = SafeFourcal()
b.setdata(4, 0)
print(b.div())

