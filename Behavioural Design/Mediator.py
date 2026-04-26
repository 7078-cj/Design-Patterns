from __future__ import annotations

class ChatUser:
    mediator = None
    
    def __init__(self, name):
        self.name = name
        
    def set_mediator(self, mediator):
        self.mediator = mediator
        
    def send_message(self, message):
        print(f"{self.name} sends message: {message}")
        self.mediator.send_message(message, self)
        
    def receive(self, message):
        print(f"{self.name} receives message: {message}")
        
class Mediator:
    def __init__(self):
        self.users = []
        
    def add_user(self, user):
        self.users.append(user)
        user.set_mediator(self)
        
    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message)
                
if __name__ == "__main__":
    mediator = Mediator()
    
    user1 = ChatUser("Alice")
    user2 = ChatUser("Bob")
    user3 = ChatUser("Charlie")
    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)
    
    user1.send_message("Hello, everyone!")
    user2.send_message("Hi, Alice!")
    user3.send_message("Hey, Alice and Bob!")
    