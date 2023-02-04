#Question 4
import random

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
for i in list1:
    if i % 2 == 1 :
        list2.append(i**3)

print(list1)
print(list2)