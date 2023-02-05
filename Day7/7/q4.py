#Question-4
Integer = int(input("Give me integer:"))


try:
    for i in Integer:
     print(i)
except TypeError:
    print("not iterable")
except:
    print("You CAN'T CATCH the point")