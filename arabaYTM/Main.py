from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self):
        self.acceleration = 0
        self.velocity = 0

    @abstractmethod
    def power(self):
        pass

    def run(self):
        self.velocity += self.acceleration

    def getVelocity(self):
        return self.velocity

    def getAcceleration(self):
        return self.acceleration

class BoostCar(ABC):
    @abstractmethod
    def Boost(self):
        pass

class AirConditioner(ABC):
    @abstractmethod
    def Open(self):
        pass

class Ferrari(Car, AirConditioner, BoostCar):
    def power(self):
        self.acceleration = 10  

    def Boost(self):
        self.acceleration *= 2

    def Open(self):
        self.acceleration *= 0.8

class Tofas(Car, AirConditioner):
    def power(self):
        self.acceleration = 5  

    def Open(self):
        self.acceleration *= 0.8

class Mercedes(Car, AirConditioner, BoostCar):
    def power(self):
        self.acceleration = 7 

    def Boost(self):
        self.acceleration *= 2

    def Open(self):
        self.acceleration *= 0.8

def main():
    ferrari = Ferrari()
    ferrari.power()
    print("Aracın ilk hızı:", ferrari.getVelocity())
    
    ferrari.run()
    print("Çalıştıktan sonraki hızı:", ferrari.getVelocity())
    
    ferrari.Boost()
    ferrari.run()
    print("Boost'tan sonraki hızı:", ferrari.getVelocity())
    
    ferrari.Open()
    ferrari.run()
    print("Klima çalıştıktan sonraki hızı:", ferrari.getVelocity())

if __name__ == '__main__':
    main()
