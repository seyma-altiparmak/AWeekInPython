#FUNCTION PRACTICE#

listBank = []

menu = """
***********************
1. Select your account:
2. Call X:
3. Delete your account:
4. Quit
***********************
"""

def selectAccount(bankCode):
    id = input("ID Please")
    print("""
    True,Your bank account code is {}
    """.format(bankCode))

def Call(X):
    return ("Called.")

def deleteAccount(backCode,isDeleted):
    if isDeleted:
        listBank.remove(backCode)


def Quit():
    quit()

def MH():
    print(menu)
    select = int(input("Choose:"))
    if select ==1:
        BK=input("Enter BankCode:")
        selectAccount(BK)
    elif select==2:
        number = input("Enter you call assistan 1 / 2 :")
        print(Call(number))
    elif select==3:
        BK=input("Enter BankCode:")
        x = input(bool("U sure [Y] or [N] :"))
        deleteAccount(BK,x)
        print("Deleted {x}.".format(x=BK))
    elif select==4:
        Quit()
    else:
        print("UNDEFINED.")

while True:MH()