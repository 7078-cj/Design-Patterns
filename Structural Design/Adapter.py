from dataclasses import dataclass

@dataclass
class DisplayDataType:
    index: float
    data: str
    
class DisplayData:
    def __init__(self, data: DisplayDataType):
        self.display_data = data

    def display(self):
        print(f"Index: {self.display_data.index}, Data: {self.display_data.data}")
        

@dataclass
class DatabaseDataType:
    position: int
    amount: int
    
class StoreDatabaseData:
    def __init__(self, data: DatabaseDataType):
        self.data = data

    def store(self):
        print(f"Position: {self.data.position}, Amount: {self.data.amount}")
        

class DisplayDataAdapter(DisplayData, StoreDatabaseData):
    def __init__(self, data):
        self.data = data
        
    def store_data(self):
        for item in self.data:
            ddt = DisplayDataType(float(item.position), str(item.amount))
            self.display_data = DisplayData(ddt)
            self.display_data.display()  
            

def generate_data():
    return [
        DatabaseDataType(position=1, amount=100),
        DatabaseDataType(position=2, amount=200),
        DatabaseDataType(position=3, amount=300),
    ]

if __name__ == '__main__':
    data = generate_data()
    adapter = DisplayDataAdapter(data)
    adapter.store_data()