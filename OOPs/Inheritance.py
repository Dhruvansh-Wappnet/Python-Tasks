'''# Single Level Inheritance*****************************************
class Parent:
    def __init__(self):
        print("Parent constructor")

    def parent_method(self):
        print("Parent method")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

    def child_method(self):
        print("Child method")


# Creating an instance of Child
child_obj = Child()
# Accessing methods from both Parent and Child
child_obj.parent_method()
child_obj.child_method()'''

'''# Multiple Inheritance*********************************************
class Parent1:
    def __init__(self):
        print("Parent1 constructor")
        
    def method1(self):
        print("Method from Parent1")


class Parent2:
    def __init__(self):
        print("Parent2 constructor")
    
    def method2(self):
        print("Method from Parent2")


class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        Parent2.__init__(self)
        print("Child constructor")
        
    def method3(self):
        print("Method from Child")


# Creating an instance of Child
child_obj = Child()
# Accessing methods from all three classes
child_obj.method1()
# child_obj.method2()
# child_obj.method3()'''

'''
# Multi Level Inheritance******************************************
class Grandparent:
    def __init__(self):
        print("Grandparent constructor")

    def method1(self):
        print("Method from Grandparent")


class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent constructor")
        
    def method2(self):
        print("Method from Parent")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")
        
    def method3(self):
        print("Method from Child")


# Creating an instance of Child
child_obj = Child()
# Accessing methods from all three classes
child_obj.method1()
child_obj.method2()
child_obj.method3()

# Hierarchical Inheritance******************************************
class Parent:
    def __init__(self):
        print("Parent constructor")
    
    def method1(self):
        print("Method from Parent")


class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("Child1 constructor")
        
    def method2(self):
        print("Method from Child1")


class Child2(Parent):
    def __init__(self):
        super().__init__()
        print("Child2 constructor")
        
    def method3(self):
        print("Method from Child2")


# Creating instances of Child1 and Child2
child1_obj = Child1()
child2_obj = Child2()
# Accessing methods from respective classes
child1_obj.method1()
child1_obj.method2()
child2_obj.method1()
child2_obj.method3()
'''
# Hybrid Inheritance*******************************************
class Animal:
    def __init__(self):
        print("Animal constructor")

    def eat(self):
        print("Animal is eating")


class Mammal(Animal):
    def __init__(self):
        print("In mammal")
        super().__init__()
        print("Mammal constructor")

    def sleep(self):
        print("Mammal is sleeping")


class Bird(Animal):
    def __init__(self):
        print("In Bird")
        super().__init__()
        print("Bird constructor")
        
    def fly(self):
        print("Bird is flying")


class Dog(Mammal):
    def __init__(self):
        super().__init__()
        print("Dog constructor")
        
    def bark(self):
        print("Dog is barking")


class Bat(Mammal, Bird):
    def __init__(self):
        super().__init__()
        print("Bat constructor")
        
    def hang(self):
        print("Bat is hanging")

dog = Dog()
bat = Bat()
dog.sleep() 
dog.bark() 
print()
bat.eat()   
bat.sleep() 
bat.fly()  
bat.hang()