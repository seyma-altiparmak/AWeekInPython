# I T E R A T O R #
#integers not iterable
#iter - next => iterable methods

# G E N E R A T O R
def l():
    for i in range(1,10):
        yield i**3

# L I S T  C O M.
liste = [i**3 for i in range(1,5)]

#D E C O R A T O R
def decorator():
    print("DECORATOR")

@decorator
def fonksiyon():
    print("working...")