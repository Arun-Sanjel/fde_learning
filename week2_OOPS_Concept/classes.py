# OOPS concept

class Employee:
    
    # constructor
    # initiaiizing variables 

    def __init__(self,first , last, pay):
        # self.variable = arg

        self.first = first
        self.last = last
        self.email = first.lower() + '.' +last.lower() +'@gmail.com'
        self.pay = pay


    def fullname(self):
        return self.first + ' ' + self.last

    
emp1 = Employee('Arun', 'Sanjel', 5000)
emp2 = Employee('Heroic', 'Crazy', 4000)


print("THe email is ", emp1.email)
print("THe full name is ", emp1.fullname(), "\n")

print("THe email  of the ace is ", emp2.email)
print("THe full name is ", emp2.fullname())


