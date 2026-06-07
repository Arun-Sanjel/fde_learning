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
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount #it plays with the cls - > class and its funciton and variabes

    
    @classmethod
    def from_string(cls, emp_str):
        first,last, pay = emp_str.split(',')
        return cls(first,last,pay)
    

    # static method

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True





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


# setting raise amt
Employee.set_raise_amt(1.08) #it changes the entire value of global raise amt

# testing with
print("this is the employee class raise amt" , Employee.raise_amt)
print("THis is the emp1 int raise amt", emp1.raise_amt)
print("this is the emp2 int raise amt", emp2.raise_amt)

print("the final cls is ", emp1.from_string('rurnoune,kenshin,2000'))

# static method
import datetime

my_date = datetime.date(2026,7,13)

print(Employee.is_workday(my_date))



