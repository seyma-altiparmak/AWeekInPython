# BASIC CALCULATOR
number1 = int(input("number 1 :"))
number2 = int(input("number 2 :"))
a = input("+ , / , * , -")

if a=="+":
    print(number1+number2)
elif a=="-":
    print(number1-number2)
elif a=="/":
    print(number1/number2)
elif a=="*":
    print(number1*number2)
else:
    print("UNDEF.")