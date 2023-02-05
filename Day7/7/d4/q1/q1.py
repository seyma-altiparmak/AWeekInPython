class Company():
    #one company
    companyID = "#451236"
    def __init__(self,name ="",companyTYPE= ""):
        self.name = name
        self.companyTYPE = companyTYPE

class Person(Company):
    def __init__(self, companyID,personNO ,personname,persontype):
        self.companyID = companyID
        self.personNO = personNO
        self.personname = personname
        self.persontype = persontype
    @classmethod
    def Senior(cls):
        def __init__(self,projects = 0):
            self.projects = projects
            projects +=10
        @staticmethod
        def SayNAME(personName=" "):
            if Person.personname == False:
                raise Exception("NO NAME PERSON")
            else:
                return Person.personname
    @classmethod
    def Mid(cls):
        def __init__(self,projects=0):
            self.projects = projects
            projects +=5
        def SayNAME(personName=" "):
            if Person.personname == False:
                raise Exception("NO NAME PERSON")
            else:
                return Person.personname
    @classmethod
    def Junior(cls):
        def __init__(self,projects= 0):
           self.projects = projects
           projects +=2
        def SayNAME(personName=""):
            if Person.personname == False:
                raise Exception("NO NAME PERSON")
            else:
                return Person.personname

class Intern(Person):
    def __init__(self, companyID = "#45465", personNO = 0, personname="", persontype="",school="$451"):
        super().__init__(companyID, personNO, personname, persontype)
        self.school = school
