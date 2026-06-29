class Student:
    def __init__(self,name,branch,age):
        self.name=name
        self.branch=branch
        self.age=age
    def display_info(self):
        print("Name: ",self.name)
        print("Branch: ",self.branch)
        print("Age: ",self.age)
    def study(self):
        print("Good!")
        
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount deposited successfully!")
    def withdraw(self,amount):
        if(amount>self.balance): 
            print("Balance insufficient!")
        else:   
            self.balance=self.balance-amount
            print("Amount withdrwan successfully!")
    def show_balance(self):
        print("Your bank account has ",self.balance,"rs. currently!")
    
class Car:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed
    def accelerate(self):
        self.speed+=10
        print("Car accelerated!")
    def brake(self):
        self.speed-=10
        print("Car stopped!")
        
class LibraryBook:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def borrow(self):
        print("Book borrowed!")
    def return_book(self):
        print("Book returned!")

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def increment(self,increment):
        self.salary=self.salary+(increment/100)*self.salary
    def display(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)
        
s1=Student("Alice","CS",20)
s1.display_info()
s1.study()

b1=BankAccount("Bob",1200)
b1.deposit(300)
b1.withdraw(1600)
b1.deposit(500)
b1.withdraw(1500)
b1.show_balance()

c1=Car("Hyundai","SUV",40)
c1.accelerate()
c1.brake()

l1=LibraryBook("Love hypothesis","Ali Hazelwood")
l1.borrow()
l1.return_book()

e1=Employee("Calor",1000)
e1.display()
e1.increment(10)
e1.display()