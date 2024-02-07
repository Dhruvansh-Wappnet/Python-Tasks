# ---------------------------------------------Abstraction---------------------------------------------------------

# from abc import ABC,abstractmethod

# class Car(ABC):
#     @abstractmethod
#     def mileage(self):
#         x = 10
#         print(x)

# class Tesla(Car):
#     def start(self):
#         print("Car is starting.")
#     def mileage(self):
#         super().mileage()

# class Suzuki(Car):
#     def mileage(self):
#         print("The mileage is 25kmph.")


# obj_suzuki = Suzuki()
# obj_suzuki.mileage()
# print()

# obj_tesla = Tesla()
# obj_tesla.start()
# obj_tesla.mileage()


# obj_car = Car()
# obj_car.mileage()
# ---------------------------------------------Abstraction---------------------------------------------------------

# --------------------------------------------Encapsulation-------------------------------------------------------
# class Person:
#     def __init__(self, name, age, email):
#         self._name = name
#         self._age = age
#         self.__email = email

#     def get_email(self):
#         return self.__email

#     def set_email(self, email):
#         # Perform validation if needed
#         self.__email = email

#     def get_name(self):
#         return self._name

#     def get_age(self):
#         return self._age

# class Employee(Person):
#     def __init__(self, name, age, email, salary):
#         super().__init__(name, age, email)
#         self._salary = salary

#     def display_employee(self):
#         print(f"Name : {self.get_name()} \nAge : {self.get_age()} \nEmail : {self.get_email()} \nSalary : {self._salary}")

# class Car():
#     def  __init__(self, make, model, year):
#         self._make = make
#         self._model = model
#         self._year = year
#         self._mileage = None

#     def mileage(self):
#         print(f"This car has been driven {self.mileage} miles.")

# # emp = Employee("dp",21,"test@gmail.com",1000)
# # emp.set_email("abc@gmail.com")
# # emp.display_employee()
# print()

# person = Person("Ali", 20, "ali@example.com")
# # person.__email = "abc@gmail.com"
# # person.set_email("abc@gmail.com")
# person.__email  = "xyz@example.com"
# # Accessing data through methods
# # print("Name:", person.get_name())
# # print("Age:", person.get_age())
# # print("Email:", person.get_email())
# print(person.__email)
# print(person._Person__email)

# Attempting to access the email directly
# This will raise an AttributeError
# print(person._email)
# -----------------------------------------------Encapsulation-----------------------------------------------------

# -----------------------------------------------Access Modifiers---------------------------------------------------

# Public***************************************************************

# class Teacher:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def dispPublicMembers(self):
#         print("This is public member: ", self.name, self.salary)


# # t1 = Teacher("Simon", 12500)
# # print(t1.name)
# # print(t1.salary)
# # t1.dispPublicMembers()

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def dispPublicMember(self):
#         print("This is public member: ", self.name, self.age)
    
#     teacher = Teacher("Mr. Smith", 8000)
    
#     def dispTeacherMember(self):
#         self.teacher.dispPublicMembers()
    
# s1 = Student("Jack",22)
# s1.dispPublicMember()
# s1.dispTeacherMember()      


# Protected***************************************************************

# class Teacher:
#     def __init__(self,name,salary):
#         self._name=name
#         self._salary=salary
        
#     def _dispProtectedMembers(self):
#         print("This is public member: ", self._name, self._salary)
        
# # t2=Teacher("Simon", 12500)
# # print(t2._name)
# # print(t2._salary)
# # t2._dispPrivateMembers()

# class Student:
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age
        
#     def _dispProtectedMember(self):
#         print("This is public member: ", self._name, self._age)
        
#     teacher = Teacher("Mr. Smith", 8000)
        
#     def dispTeacherMember(self):
#         self.teacher._dispProtectedMembers()
        
        
# s2 = Student( "John Doe" , 23)
# s2._dispProtectedMember()
# s2.dispTeacherMember()

# Private*****************************************************************

# class Teacher:
#     def __init__(self,name,salary):
#         self.__name=name
#         self.__salary=salary
        
#     def __dispPrivateMembers(self):
#         print("This is public member: ", self.__name, self.__salary)
        
# # t2=Teacher("Simon", 12500)
# # print(t2.__name)
# # print(t2.__salary)
# # t2.__dispPrivateMembers()

# class Student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
        
#     def __dispPrivateMember(self):
#         print("This is public member: ", self.__name, self.__age)
        
#     teacher = Teacher("Mr. Smith", 8000)
        
#     def dispTeacherMember(self):
#         self.teacher.__dispPrivateMembers()
        
        
# s2 = Student( "John Doe" , 23)
# s2.__dispPrivateMember()
# s2.dispTeacherMember()

        
# -----------------------------------------------Access Modifiers---------------------------------------------------

# -----------------------------------------------Inheritance-------------------------------------------------------

