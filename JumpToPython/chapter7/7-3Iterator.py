import time

class MyItertor:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyItertor([1,2,3])
    for item in i:
        print(item)
        
class ReverseItertor:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

if __name__ == "__main__":
    i = ReverseItertor([1,2,3])
    for item in i:
        print(item)
        
        
# 제너레이터(generator)는 이터레이터를 생성해 주는 함수이다. 
# 제너레이터로 생성한 객체는 이터레이터와 마찬가지로 next 함수 호출 시 그 값을 차례대로 얻을 수 있다. 
# 이때 제너레이터에서는 차례대로 결과를 반환하고자 return 대신 yield 키워드를 사용한다.


def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))

def longtime_job():
    print("job start")
    time.sleep(0.1)  # 1초 지연
    return "done"

# list_job = [longtime_job() for i in range(5)]
# print(list_job[0])

#실행할때마다 수행되기 때문에 디멘드 페이징 느낌이다.
list_job = (longtime_job() for i in range(5))
print(next(list_job))