from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    
    @abstractmethod
    def make_small_coffee(self):
        pass
    
    @abstractmethod
    def make_large_coffee(self):
        pass
    
class BasicCoffeeMachine(CoffeeMachine):
    
    def make_small_coffee(self):
        print("Making small coffee")
        
    def make_large_coffee(self):
        print("Making large coffee")
        
class CoffeeMachineDecorator(CoffeeMachine):
    
    def __init__(self, basic_machine: BasicCoffeeMachine):
        self.basic_machine = basic_machine
        
    def make_small_coffee(self):
        self.basic_machine.make_small_coffee()
        
    def make_large_coffee(self):
        print("Adding extra flavor")
        self.basic_machine.make_large_coffee()
        
    def make_milk_coffee(self):
        print("Making milk coffee")
        self.basic_machine.make_small_coffee()
        print("enhanced with milk")
        
if __name__ == '__main__':
    basic_machine = BasicCoffeeMachine()
    decorated_machine = CoffeeMachineDecorator(basic_machine)
    
    decorated_machine.make_small_coffee()
    print()
    decorated_machine.make_large_coffee()
    print()
    decorated_machine.make_milk_coffee()