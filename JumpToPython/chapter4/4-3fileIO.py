# file 입출력 

f = open("JumpToPython/chapter4/새파일.txt", 'w')
f.close()

f = open("새파일.txt", 'w')
f.close()

f = open("JumpToPython/chapter4/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("JumpToPython/chapter4/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("JumpToPython/chapter4/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
f.close()

f = open("JumpToPython/chapter4/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

print("read")
f = open("JumpToPython/chapter4/새파일.txt", 'r')
file = f.read()
print(file)
f.close()


print("append")
f = open("JumpToPython/chapter4/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
print(file)
f.close()

print("read")
f = open("JumpToPython/chapter4/새파일.txt", 'r')
file = f.read()
print(file)
f.close()

