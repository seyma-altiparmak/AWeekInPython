# C L A S S :
import time
#smart oven project:

class Oven():
    ovenType = "Siram"
    ovenTimer = "Dynamic"

    def __init__(self,ID=0,ModelYear=0,Color=""):
        ID +=10
        self.ID = ID
        self.ModelYear = ModelYear
        self.Color = Color

    def timer(function):
        def Ttimer(*args,**kwargs):
            start = time.time()
            function(*args,**kwargs)
            end = time.time()
            print (f"Machine timer is {end-start}")
        return Ttimer

    @timer
    def newModel(self,model):
        self.ModelYear = model

    def __str__(self):
        return f"Model = {self.ModelYear} ID = {self.ID}"

    def __len__(self):
        return self.ID

    @timer
    def __add__(self,other):
        return self.ModelYear + other.ModelYear

    #iterable: and at the same 
    #i can add (__next__)
    def __iter__(self):
        return self

    def generator(self):
        for i in range(1,self.ModelYear):
            yield 2*i

    @classmethod
    def numberOfOven(cls):
        return cls.ID

    @staticmethod
    def sayOvenType():
        return Oven.ovenType

Marcel = Oven()