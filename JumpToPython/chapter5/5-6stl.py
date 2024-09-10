#표준 라이브러리

import datetime
import time

day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

print(day1)
print(day2)

diff = day2 - day1
print(diff.days)
print(day2.weekday())

a = time.time()

for i in range(1000):
    time.sleep(0.0001)
    pass
    #print("")

b = time.time()
print(b-a)