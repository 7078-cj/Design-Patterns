class Equipment:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
        
class Composite:
    def __init__(self,name:str):
        self.name = name
        self.items = []
        
    def add(self, equipment: Equipment):
        self.items.append(equipment)
        return self
    
    @property
    def price(self):
        total_price = sum(item.price for item in self.items)
        return total_price
    
    @price.setter
    def price(self, value):
        self._price = value
        
if __name__ == '__main__':
    computer = Composite("PC")
    processor = Equipment("Processor", 250.0)
    ram = Equipment("RAM", 150.0)
    hard_drive = Equipment("Hard Drive", 100.0)
    memory = Composite("Memory")
    rom = Equipment("ROM", 50.0)
    ram2 = Equipment("RAM", 150.0)
    
    mem = memory.add(rom).add(ram2)
    pc = computer.add(processor).add(ram).add(hard_drive).add(mem)
#  PC
#  ├── Processor (250)
#  ├── RAM (150)
#  ├── Hard Drive (100)
#  └── Memory in here when the loop it calls 
#       ├           price it will call the price of memory and 
#       ├           it will sum the price of rom and ram2
#       ├── ROM (50)
#       └── RAM (150)
    
    
    print(f"{computer.name} Price: {computer.price}")