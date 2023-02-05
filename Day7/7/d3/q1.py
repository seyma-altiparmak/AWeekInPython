#Question-1:
#*args
def product(*args):
    result = 1 #start
    for i in args:
        result = result*i
    return result

print(product(5,50,2,10))