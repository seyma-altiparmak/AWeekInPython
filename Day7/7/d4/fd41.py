#Class & Object

class work():
    pass

doctor = work()

doctor.name="DR"
doctor.isIll = False
doctor.hospital = "Devlet Hastanesi"

print(doctor.name)

#init
class worker():
    def __init__(self,name,work):
        self.name = name
        self.work = work

worker1 = worker("April","Singer")
print(worker1.name + worker1.work)

#standard mood:
class days():
    def __init__(self,best="Monday",worst="Tuesday",average = "Sunday"):
        self.best = best
        self.worst = worst
        self.average = average
        # M e t h o d s:
    def see(self):
        return (f"best day is {self.best} worst day is {self.worst} average is {self.average}")


worker1.day = days()
print(worker1.day.see())

#V A R I A B L E S - I N S T A N C E :
class bookmarket():
    #V a r i a b l e:
    city = "L.A."
    #I n s t a n c e:
    def __init__(self,booknum = 0, bookname = "", culture =""):
        self.booknum =booknum
        self.booknum +=  10
        bookmarket.booknum = self.booknum #ID
        self.bookname = bookname
        self.culture = culture

    @classmethod
    def howMBook(cls):
        return bookmarket.booknum

AStore = bookmarket(5,"Ad","Sa")
print(AStore.howMBook())