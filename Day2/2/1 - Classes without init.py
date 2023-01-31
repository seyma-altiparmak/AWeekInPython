#CLASS out init:#

#Student class
class Student():
    name = ''
    number = 0
    age = 0
    notes = []

#Teacher class
class Teacher():
    student = Student() 
    name = ''
    age = 0
    classes = []


aisia = Student()
aisia.name = "Aisia"
aisia.age = 15
aisia.notes = 5
aisia.number = 10464
############################
hailey = Teacher()
hailey.student = aisia.name
hailey.classes += "A"
hailey.name = "Baby"
#############################
yunus = Teacher()
yunus.student = hailey.name
yunus.classes += "B","C"
yunus.name = "Shark"

print(hailey.name,hailey.classes,hailey.student,hailey.age)
print(yunus.name,yunus.classes,yunus.student,yunus.age)
# BABY SHARK DO DO DO