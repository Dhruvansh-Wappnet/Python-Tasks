# Example 1
# '''
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
cow = Cow()

print(animal_sound(dog))
print(animal_sound(cat))
print(animal_sound(cow))
# '''

# Example 2
'''
class Vehicle:
    def fuel_efficiency(self):
        pass

class Car(Vehicle):
    def __init__(self, fuel_capacity, miles_driven, fuel_used):
        self.fuel_capacity = fuel_capacity
        self.miles_driven = miles_driven
        self.fuel_used = fuel_used

    def fuel_efficiency(self):
        return self.miles_driven / self.fuel_used

class Bicycle(Vehicle):
    def __init__(self, miles_traveled, calories_burned):
        self.miles_traveled = miles_traveled
        self.calories_burned = calories_burned

    def fuel_efficiency(self):
        return float('inf') if self.calories_burned == 0 else self.miles_traveled / self.calories_burned

class Plane(Vehicle):
    def __init__(self, fuel_capacity, distance_traveled):
        self.fuel_capacity = fuel_capacity
        self.distance_traveled = distance_traveled

    def fuel_efficiency(self):
        return self.distance_traveled / self.fuel_capacity

def calculate_efficiency(vehicle):
    return vehicle.fuel_efficiency()

car = Car(fuel_capacity=50, miles_driven=500, fuel_used=25)
bicycle = Bicycle(miles_traveled=100, calories_burned=500)
plane = Plane(fuel_capacity=1000, distance_traveled=5000)

print("Car fuel efficiency:", calculate_efficiency(car))  
print("Bicycle fuel efficiency:", calculate_efficiency(bicycle))  
print("Plane fuel efficiency:", calculate_efficiency(plane))  
'''

'''
# Method Overloading        In python method overloading is not supported as the latest method in same class will overrides the all above method with same name.
class MathOperations:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c ):
        return a + b + c

math_ops = MathOperations()

print(math_ops.add(2, 3))
print(math_ops.add(2, 3, 4))'''
