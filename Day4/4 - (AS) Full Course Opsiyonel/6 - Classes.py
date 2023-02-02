#CLASS
class A:
    def __init__(self,age):
        self.age = age

    def die(self):
        return ("Alive!")

    def __len__(self):
        print(self.age)

#inherit
class B(A):
    def __init__(self, age):
        super().__init__(age)

james = A(15)

print(("james age is {}").format(str(james.age)))
print("James is " + str( james.die()))
james.__len__()

# https://github.com/atilsamancioglu/PythonCourse/blob/master/03-StringsAdvanced.ipynb