# OOPS concept

class Employee:

    # defining variables --> global variables
    num_of_emp = 10
    raise_amt = 1.04
    
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

    # def apply_raise(self , amt):
    #     return self.pay+ self.pay * amt/100
    
    def apply_raise( self):
        return self.pay * self.raise_amt
    
emp1 = Employee('Arun', 'Sanjel', 5000)
emp2 = Employee('Heroic', 'Crazy', 4000)


print("THe email is ", emp1.email)
print("THe full name is ", emp1.fullname(), "\n")

print("THe email  of the ace is ", emp2.email)
print("THe full name is ", emp2.fullname())

# with raise arg
# print("Congratulation", emp2.first , "for your raise of ", emp2.apply_raise(5))

# without raise arg
print("Congratulation", emp2.first , "for your raise of ", emp2.apply_raise())



