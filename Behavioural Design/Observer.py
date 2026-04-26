from abc import ABC, abstractmethod


class EventListener(ABC):
    @abstractmethod
    def update(self, event_type, file):
        pass
    
class EventManager:
    def __init__(self, operations):
        self.operations = operations
        self.listeners = {}
        for op in operations:
            self.listeners[op] = []
            
    def subscribe(self, event_type, listener):
        users = self.listeners.get(event_type)
        if listener not in users:
            users.append(listener)
    
    def unsubscribe(self, event_type, listener):
        users = self.listeners.get(event_type)
        if listener in users:
            users.remove(listener)
    
    def notify(self, event_type, file):
        users = self.listeners.get(event_type)
        for listener in users:
            listener.update(event_type, file)
            
class Editor:
    events = EventManager(["open", "save"])
    file = None
    
    def open_file(self, file_path):
        self.file = file_path
        print(f"Editor: Opening file {self.file}")
        self.events.notify("open", self.file)
        
    def save_file(self):
        if self.file:
            print(f"Editor: Saving file {self.file}")
            self.events.notify("save", self.file)
        else:
            print("Editor: No file to save.")
            
class EmailNotificationListener(EventListener):
    def __init__(self, email):
        self.email = email
        
    def update(self, event_type, file):
        print(f"Email to {self.email}: Someone has performed {event_type} operation on the file {file}")

class LogOpenListener(EventListener):
    def __init__(self, log_file):
        self.log_file = log_file
    
    def update(self, event_type, file):
        print(f"Logging: Save to log {self.log_file}: Someone has performed {event_type} operation on the file {file}")
        
if __name__ == "__main__":
    editor = Editor()
    
    email_listener = EmailNotificationListener("test@gmail.com")
    log_listener = LogOpenListener("test.file")
    
    editor.events.subscribe("open", log_listener)
    editor.events.subscribe("save", log_listener)
    editor.events.subscribe('save', email_listener)
    
    editor.open_file("test.txt")
    editor.save_file()
    