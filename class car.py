from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def __init__(self, name, num_wheels):
        self.name = name
        self.num_wheels = num_wheels
    @abstractmethod
    def display_details(self):
        pass
class Car(Vehicle):
    def __init__(self, name, num_doors):
        super().__init__(name, 4)
        self.num_doors = num_doors
    def display_details(self):
        print('Name: {}'.format(self.name))
        print('Number of wheels: {}'.format(self.num_wheels))
        print('Number of doors: {}'.format(self.num_doors))
class Motorcycle(Vehicle):
    def __init__(self, name, has_sidecar):
        super().__init__(name, 2)
        self.has_sidecar = has_sidecar
    def display_details(self):
        print('Name: {}'.format(self.name))
        print('Number of wheels: {}'.format(self.num_wheels))
        print('Has sidecar: {}'.format(self.has_sidecar))

class Truck(Vehicle):
    def __init__(self, name, payload_capacity):
        super().__init__(name, 6)
        self.payload_capacity = payload_capacity
    def display_details(self):
        print('Name: {}'.format(self.name))
        print('Number of wheels: {}'.format(self.num_wheels))
        print('Payload capacity: {}'.format(self.payload_capacity))
    def main():
        car = Car('Honda Civic', 4)
        car.display_details()
        print()
        motorcycle = Motorcycle('Harley Davidson', False)
        motorcycle.display_details()
        print()
        truck = Truck('Ford F-150', 3000)
        truck.display_details()
    if __name__ == '__main__':
        main()
