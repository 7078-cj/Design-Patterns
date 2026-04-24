from abc import ABC, abstractmethod

class Device(ABC):
    volume = 0
    
    @abstractmethod
    def get_name(self)->str:
        pass
    
    
class Radio(Device):
    def get_name(self) -> str:
        return f"Radio {self}"
    
class TV(Device):
    def get_name(self) -> str:
        return f"TV {self}"
    
class Remote(ABC):
    
    @abstractmethod
    def volume_up(self):
        pass
    
    @abstractmethod
    def volume_down(self):
        pass
    
class BasicRemote(Remote):
    def __init__(self, device: Device):
        self.device = device
        
    def volume_up(self):
        self.device.volume += 1
        print(f"{self.device.get_name()} Volume: {self.device.volume}")
        
    def volume_down(self):
        self.device.volume -= 1
        print(f"{self.device.get_name()} Volume: {self.device.volume}")
        
if __name__ == '__main__':
    radio = Radio()
    tv = TV()
    
    remote1 = BasicRemote(radio)
    remote2 = BasicRemote(tv)
    
    remote1.volume_up()
    remote1.volume_up()
    remote1.volume_down()
    
    remote2.volume_up()
    remote2.volume_down()