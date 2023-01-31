import random


class Reporter:

    def _init_(self, name, surname, show):
        self.name = name
        self.surname = surname
        self.show = show

    def chanel(self):
        print("""
        Chanel is {x} and its id = {y} 
        """).__format__(x=chanel.name, y=chanel.ID)


class Chanel:

    def _init_(self):
        self.name = ' '
        self.ID = random.randint(0, 100)
        self.reporterName = ' '

    def chanel(self):
        print("""
        Reporter is {x} and its SHOW = {y} 
        """).__format__(x=reporter.name + reporter.surname, y=reporter.show)

reporter = Reporter()
chanel = Chanel()