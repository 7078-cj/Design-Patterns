from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, command_id):
        self.command_id = command_id
    
    @abstractmethod
    def execute(self):
        pass
    
class OrderAddCommand(Command):
    def __init__(self, command_id, order_details):
        super().__init__(command_id)
        self.order_details = order_details
        
    def execute(self):
        print(f"Executing OrderAddCommand: Adding order with details: {self.order_details} for {self.command_id}")
        
class OrderPayCommand(Command):
    def __init__(self, command_id, order_id):
        super().__init__(command_id)
        self.order_id = order_id
        
    def execute(self):
        print(f"Executing OrderPayCommand: Paying for order with ID: {self.order_id} for {self.command_id}")

class CommandProcessor:
    queue = []
    
    def add_to_queue(self, command):
        self.queue.append(command)
    
    def process_commands(self):
        while self.queue:
            command = self.queue.pop(0)
            command.execute()
        print("All commands processed.")
        self.queue.clear()
        
if __name__ == "__main__":
    processor = CommandProcessor()
    
    add_command = OrderAddCommand("user123", {"item": "Laptop", "quantity": 1})
    pay_command = OrderPayCommand("user123", "order456")
    
    add_command2 = OrderAddCommand("user456", {"item": "Phone", "quantity": 2})
    pay_command2 = OrderPayCommand("user456", "order789")
    
    processor.add_to_queue(add_command)
    processor.add_to_queue(pay_command)
    processor.add_to_queue(add_command2)
    processor.add_to_queue(pay_command2)
    
    processor.process_commands()
    