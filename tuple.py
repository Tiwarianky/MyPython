lists=["Radha","Mira","Sita","Gita"]
mark=(92,99,94,95,90,97,99,90,95,97,99)
""""
data=lists.sort()
dat=lists.pop(3)
new=lists.append(90)
intt=lists.insert(2,44)
print(lists)
print(lists.index(89))
print(type(mark))
print(len(mark))
print(mark[0])
print(mark.count(90))
print(mark.index(90))
"""

for name in lists:
    if name=="":
      continue
    print(name)