# 집합

s1 = set([1, 2, 3])
print(s1)
l1 = list(s1)
print(l1)

s2 = set("Hello")
print(s2)


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)

s1.update([11,12,13])
print(s1)