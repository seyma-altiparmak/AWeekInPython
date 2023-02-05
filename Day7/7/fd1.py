# if we do not return sth -> "void" function
def Welcome():
    print("welcome")
    #you should have call.
Welcome()

def pii(num1,num2):
    if num1>num2:
        print("pii :O")

pii(5,4)

diil = pii #equal sth
diil(10,5)

#Args
def worker(*info): #infos no have num.
    print("infos:")
    for i in info:
        print(i)

worker("sym","SA",21)

#Keywords
def workers(**infos):
    print("surname", infos["surname"])
    print("name", infos["name"])
    print("id", infos["id"])

workers(name = "sym",surname = "al" , id = 555555)

#return:
def sum(x,y):
    return x+y

sum(10,20)

#pass:
def bos():
    pass

#lambda:
def crp(x,y):
    pass
crp = lambda x,y: print(x*y)
crp(5,6)