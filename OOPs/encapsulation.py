class Person:
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        # Perform validation if needed
        self.__email = email

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

class Employee(Person):
    def __init__(self, name, age, email, salary):
        super().__init__(name, age, email)
        self._salary = salary

    def display_employee(self):
        print(f"Name : {self.get_name()} \nAge : {self.get_age()} \nEmail : {self.get_email()} \nSalary : {self._salary}")

class Car():
    def  __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = None

    def mileage(self):
        print(f"This car has been driven {self.mileage} miles.")

# emp = Employee("dp",21,"test@gmail.com",1000)
# emp.set_email("abc@gmail.com")
# emp.display_employee()
print()

person = Person("Ali", 20, "ali@example.com")
# person.__email = "abc@gmail.com"
# person.set_email("abc@gmail.com")
person.__email  = "xyz@example.com"
# Accessing data through methods
# print("Name:", person.get_name())
# print("Age:", person.get_age())
# print("Email:", person.get_email())
print(person.__email)
print(person._Person__email)

#Attempting to access the email directly
#This will raise an AttributeError
print(person._email)