import re
email_pattern  = '[\w\.-]+@[\w\.-]+\.\w+'

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.__email = ""
        
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if re.fullmatch(email_pattern,email):   
            self.__email = email
        else:
            print("Invalid Email")
            
person = Person("John Doe", 30)
print(person.get_name())
print(person.get_age())

person.__email = "abc.gmail.com"
print(person.__email)          # This creates a new attribute, doesn't affect the __email attribute inside the class.
print(person.get_email())            #It will print nothing as email is not set by set method
# person._age = 35
# print(person.get_age())

person.set_email("john.doe@example.com")
print(person.get_email())
person.set_email("abc.gmail.com")
print(person.get_email())