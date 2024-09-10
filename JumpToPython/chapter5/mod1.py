def add(a, b):
    return a + b

def sub(a, b): 
    return a-b

print(__name__)
#이건 거의 디버깅용일듯 이 파일이 메인으로 수행 되었을때만 호출되는 것임
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))