from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, speed, fuel_level):
        self._speed = speed
        self._fuel_level = fuel_level

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, (int, float)):
            raise ValueError("speed must be a number")
        if speed < 0:
            raise ValueError("speed must be a non-negative number")
        self._speed = speed

    @property
    def fuel_level(self):
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, fuel_level):
        if not isinstance(fuel_level, (int, float)):
            raise ValueError("fuel_level must be a number")
        if fuel_level < 0:
            raise ValueError("fuel_level must be a non-negative number")
        self._fuel_level = fuel_level

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def fuel_efficiency(self):
        pass


class Car(Vehicle):
    def __init__(self, speed, fuel_level):
        super().__init__(speed, fuel_level)

    def accelerate(self):
        self.speed += 10
        self.fuel_level -= 1
        print(f"Car accelerates to {self.speed} km/h. Fuel level: {self.fuel_level}L.")

    def brake(self):
        self.speed = max(0, self.speed - 10)
        print(f"Car slows down to {self.speed} km/h.")

    def fuel_efficiency(self):
        efficiency = 15 - (self.speed / 100) * 5
        print(f"Car fuel efficiency: {efficiency} km/L.")
        return efficiency


class Truck(Vehicle):
    def __init__(self, speed, fuel_level, load):
        super().__init__(speed, fuel_level)
        self._load = load

    @property
    def load(self):
        return self._load

    @load.setter
    def load(self, load):
        if not isinstance(load, (int, float)):
            raise ValueError("load must be a number")
        if load < 0:
            raise ValueError("load must be a non-negative number")
        self._load = load

    def accelerate(self):
        slowdown = self.load * 0.005
        self.speed += 5 - slowdown
        self.fuel_level -= 3 + slowdown
        print(f"Truck accelerates to {self.speed} km/h. Fuel level: {self.fuel_level}L.")

    def brake(self):
        slowdown = self.load * 0.005
        self.speed = max(0, self.speed - 5 - slowdown)
        print(f"Truck slows down to {self.speed} km/h.")

    def fuel_efficiency(self):
        slowdown = self.load * 0.005
        efficiency = 8 - slowdown - (self.speed / 100) * 3
        print(f"Truck fuel efficiency: {efficiency} km/L.")
        return efficiency


class Motorcycle(Vehicle):
    def __init__(self, speed, fuel_level):
        super().__init__(speed, fuel_level)

    def accelerate(self):
        self.speed += 15
        self.fuel_level -= 0.5
        print(f"Motorcycle accelerates to {self.speed} km/h. Fuel level: {self.fuel_level}L.")

    def brake(self):
        self.speed = max(0, self.speed - 15)
        print(f"Motorcycle slows down to {self.speed} km/h.")

    def fuel_efficiency(self):
        efficiency = 25 - (self.speed / 100) * 2
        print(f"Motorcycle fuel efficiency: {efficiency} km/L.")
        return efficiency


vehicles = [
    Car(speed=0, fuel_level=50),
    Truck(speed=0, fuel_level=80, load=1000),
    Motorcycle(speed=0, fuel_level=20),
]

for vehicle in vehicles:
    vehicle.accelerate()
    vehicle.brake()
    vehicle.fuel_efficiency()
    print()
