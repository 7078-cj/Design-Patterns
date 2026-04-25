from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass
    
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        print(f"Real Image: loading {filename}")
        
    def display(self):
        print(f"Real Image: displaying {self.filename}", end="")
        
class ProxyImage(Image):
    def __init__(self,filename):
        self.filename = filename
        self.real_image = None
    
    def display(self):
        print(f"Proxy image: displaying {self.filename}")
        if not self.real_image:
            print("from disk")
            self.real_image = RealImage(self.filename)
            
        else:
            print("from cache")
        self.real_image.display()
        
if __name__ == "__main__":
    image = ProxyImage("test.jpg")
    
    image.display()
    
    image.display()
        