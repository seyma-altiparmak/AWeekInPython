import math
dir(math)
print(help(math))
math.atan(5)

#rename
import select as s
s.select()

#one in lib
from math import sqrt
sqrt(5) #only sqrt in math
#easy way.

#my doc.
import fd1
fd1.crp(5,6)

#try-catch
try:
    print("x")
except:
    print("IDK")

#throw error:
x = -1
if x <0:
    raise Exception("my ex")