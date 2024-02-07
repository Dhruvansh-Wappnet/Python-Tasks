from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        x = 10
        print(x)

class Tesla(Car):
    def start(self):
        print("Car is starting.")
    # def mileage(self):
    #     super().mileage()         # If we don't use abstractmethods in the inherited class then it will raise an error

class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph.")


obj_suzuki = Suzuki()
obj_suzuki.mileage()
print()

obj_tesla = Tesla()
obj_tesla.start()
obj_tesla.mileage()


obj_car = Car()
obj_car.mileage()