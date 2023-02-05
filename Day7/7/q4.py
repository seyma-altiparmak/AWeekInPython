#Question-4
Integer = int(input("Give me integer:"))

for i in Integer:
    try:
        print(i)
    except TypeError:
        print("not iterable")
    except:
        print("You CAN'T CATCH the point")