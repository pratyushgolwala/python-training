from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Light(Device):
    def turn_on(self):
        return "Light is turned on"

class AC(Device):
    def turn_on(self):
        return "AC is turned on"

class TV(Device):
    def turn_on(self):
        return "TV is turned on"
    
class RemoteControl():
    def activate(self, device:Device):
        return device.turn_on()
    
remote = RemoteControl()

devices = [Light(), AC(), TV()]

for device in devices:
    print(remote.activate(device))