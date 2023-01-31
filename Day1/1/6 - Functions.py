#FUNCTIONS#
#Calculator with Function#

# function with print:
def plus(firstNum,secondNum):
    plusNum = firstNum + secondNum
    print(plusNum)

plus(4,5) #print in function

# function with return:
def minus(firstNum,secondNum):
    minusNum = firstNum - secondNum
    return minusNum

print(minus(5,4)) #print + return 

def divide(firstNum,secondNum):
    dividedNum = int(firstNum/secondNum)
    return dividedNum

divide(17,8) # DON'T PRINT

def timesPro(firstNum,secondNum):
    times = firstNum * secondNum
    return times

print(timesPro(55,5)) #COMPLETED.