#내장 함수¡

#all 은 모두가 참이면 true 리턴
print(all([1, 2, 3]))
print(all([0, 2, 3]))

print(abs(-3))

#any는 하나라도 참이면 true 리턴
print(any([0, 2, 3]))

#유니코드 숫자 값을 받아 문자를 리턴
print(chr(97))
print(chr(44032))


#객체가 지닌 변수나 함수를 보여주는 함수
print(dir([1, 2, 3]))

#숫자 2개를 입력받아 몫과 나머지를 튜플로 리턴
print(divmod(7, 3))

#enum
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

#문자열을 전달받아 결과값 리턴
result = eval('divmod(4, 3)')
print(result)

a = 3
print(id(3))
print(id(a))


def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

#map은 함수와 반복가능한 데이터를 받는다.
def two_times(x): 
    return x*2
list(map(two_times, [1, 2, 3, 4]))

#반올림
print(round(4.6))
print(round(4.2))

print(sorted([3,1,2]))

#zip은 동일한 갯수로 이루어진 데이터를 묶어서 리턴하는 함수
print(list(zip([1, 2, 3], [4, 5, 6])))