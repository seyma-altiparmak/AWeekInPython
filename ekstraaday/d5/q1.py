#Question 1 :
from itertools import takewhile
# L I S T        C O M P R E H E N S I O N


class iterator():
    def __init__(self,liste) -> None:
        self.liste = liste
    
    def __iter__(self):
        return self



q1 = [i for i in range(5,15)]
for i in q1:
    print (i)


it = iter(q1)
while val := next(it):
    try:
        i = next(it)
        print (i)
    except StopIteration:
        print("Stop iteration")
        break