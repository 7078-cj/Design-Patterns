from dataclasses import dataclass

@dataclass
class Memento:
    state: str
    
class Originator:
    def __init__(self, state):
        self._state = state
    
    
    def save_to_memento(self):
        print("Saving current state to memento.")
        return Memento(self._state)
    
    def restore_from_memento(self, memento):
        print(f"Restoring state from memento: {memento.state}")
        self._state = memento.state
        
        
class Caretaker:
    def __init__(self):
        self._mementos = []
        
    def add_memento(self, memento):
        self._mementos.append(memento)
        
    def get_memento(self, index):
        return self._mementos[index]
    
if __name__ == "__main__":
    originator = Originator("State 1")
    caretaker = Caretaker()
    
    caretaker.add_memento(originator.save_to_memento())
    
    originator._state = "State 2"
    caretaker.add_memento(originator.save_to_memento())
    
    originator._state = "State 3"
    
    print(f"Current state: {originator._state}")
    
    originator.restore_from_memento(caretaker.get_memento(0))
    print(f"Restored state: {originator._state}")