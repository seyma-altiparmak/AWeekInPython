#Inheritance:
class books():
    library = "Hasan Kasim Nuri Oztekin Kutuphanesi"
    def __init__(self,NAME=" ",AUTHOR=" ",CONTENT= " "):
        self.NAME = NAME
        self.AUTHOR = AUTHOR
        self.CONTENT = CONTENT

    def __len__(self,bookpapers):
        super().__init__(bookpapers)

    def __add__(self,other):
        return self.NAME + other.NAME

    def __mul__(self,other):
        return self.NAME + " " + other.NAME

    @classmethod
    def content(cls):
        return books.CONTENT
    @staticmethod
    def saylib():
        return books.library

#super init
class bookstore(books):
    def __init__(self, NAME=" ", AUTHOR=" "):
        super().__init__(NAME, AUTHOR)

#overriding
class newbookstore(books):
    def __init__(self, NAME=" ", AUTHOR=" ", CONTENT=" "):
        super().__init__(NAME, AUTHOR, CONTENT)
    def newbookstore_(self,newbs):
        self.library = newbs