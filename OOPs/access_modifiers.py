# Public***************************************************************

class Teacher:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def dispPublicMembers(self):
        print("This is public member: ", self.name, self.salary)


# t1 = Teacher("Simon", 12500)
# print(t1.name)
# print(t1.salary)
# t1.dispPublicMembers()

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def dispPublicMember(self):
        print("This is public member: ", self.name, self.age)
    
    teacher = Teacher("Mr. Smith", 8000)
    
    def dispTeacherMember(self):
        self.teacher.dispPublicMembers()
    
s1 = Student("Jack",22)
s1.dispPublicMember()
s1.dispTeacherMember()      


# Protected***************************************************************

class Teacher:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
        
    def _dispProtectedMembers(self):
        print("This is public member: ", self._name, self._salary)
        
# t2=Teacher("Simon", 12500)
# print(t2._name)
# print(t2._salary)
# t2._dispPrivateMembers()

class Student:
    def __init__(self,name,age):
        self._name = name
        self._age = age
        
    def _dispProtectedMember(self):
        print("This is public member: ", self._name, self._age)
        
    teacher = Teacher("Mr. Smith", 8000)
        
    def dispTeacherMember(self):
        self.teacher._dispProtectedMembers()
        
        
s2 = Student( "John Doe" , 23)
s2._dispProtectedMember()
s2.dispTeacherMember()

# Private*****************************************************************

class Teacher:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
        
    def __dispPrivateMembers(self):
        print("This is public member: ", self.__name, self.__salary)
        
# t2=Teacher("Simon", 12500)
# print(t2.__name)
# print(t2.__salary)
# t2.__dispPrivateMembers()

class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        
    def __dispPrivateMember(self):
        print("This is public member: ", self.__name, self.__age)
        
    teacher = Teacher("Mr. Smith", 8000)
        
    def dispTeacherMember(self):
        self.teacher.__dispPrivateMembers()
        
        
s2 = Student( "John Doe" , 23)
s2.__dispPrivateMember()
s2.dispTeacherMember()