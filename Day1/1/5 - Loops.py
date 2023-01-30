#LOOPS

#for loop
Seyma = "ALTIPARMAK"

#for-Basic-loop
for surnameChar in Seyma:
    print(surnameChar)

#for-With-range()

#basic-range()
for numbers in range(15):
    print(numbers)
# 0 1 2 3 4 5 6 7 8 .. 14
# not include 15. 

#range()-start-end-points
for numbers in range(2,5):
    print(numbers)
# 2 3 4
# not include 5

#range()-a,b,c
for numbersHOOP in range(2,10,2):
    print(numbersHOOP)
# 2 4 6 8
# not include 10

#with---else
for x in range(5):
    print(x)
else:
    print("DONE.")

# nested - loop
for x in range(10):
  for y in Seyma:
    print(x, y)

#continue:
chars = ["a", "b", "c"]
for x in chars:
  if x == "c":
    continue
  print(x)
# apple cherry

# Empty-loop
for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement

