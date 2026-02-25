#Pros:
#   Only one instance
#   Single point of access for a resource

#Uses 
    # Network Manager
    # Database Access
    # Logging
    # Utility Classes

#Cons:
    # Resource Inefficient
    # breaks single responsibility
    # testability issues
    # state for life
    # it works only in a single thread

import time
from threading import Thread

#Naive implementation
class Singleton(type):
    _instances = {}
    
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            time.sleep(2)
            self._instances[self] = instance
        return self._instances[self]
    
class NetworkDriver(metaclass=Singleton):
    def log(self):
        print(f'{self}\n')
        
def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton

if __name__ == '__main__':
    #single thread
    # s1 = create_singleton()
    # s2 = create_singleton()
    
    #multi thread
    p1 = Thread(target=create_singleton)
    p2 = Thread(target=create_singleton)
    p1.start()
    p2.start()