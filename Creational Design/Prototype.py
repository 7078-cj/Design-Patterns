import copy
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    
    
class Square(Shape):
    def __init__(self, size):
        self.size = size
        
    def draw(self):
        print(f'Drawing a square with size {self.size}')
        
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def draw(self):
        print(f'Drawing a circle with radius {self.radius}')
        
class AbstractArt:
    def __init__(self, bg_color, shapes):
        self.bg_color = bg_color
        self.shapes = shapes
        
    def draw(self):
        print(f'Background color: {self.bg_color}')
        for shape in self.shapes:
            shape.draw()
            
if __name__ == '__main__':
    square1 = Square(5)
    circle1 = Circle(3)
    
    art1 = AbstractArt('red', [square1, circle1])
    art1.draw()
    
    # Clone art1 and modify the clone
    art2 = copy.copy(art1)
    art2.bg_color = 'blue'
    art2.shapes[0].size = 10  # Modify the size of the square in the clone
    
    print('\nCloned Art:')
    art2.draw()