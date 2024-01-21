# switch_dip_refactored.py
"""
Dependency inversion principle (DIP):
This principle states that high-level modules should not depend on low-level modules,
but both should depend on abstractions. 

To comply with the Dependency Inversion Principle, we introduce an protocol to decouple the high-level Switch class
from the low-level LightBulb class.
"""
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print(f"Switch {self.__class__.__name__} on")

    def turn_off(self):
        print(f"Switch {self.__class__.__name__} off")

class Fan(Switchable):
    def turn_on(self):
        print(f"Switch {self.__class__.__name__} on")

    def turn_off(self):
        print(f"Switch {self.__class__.__name__} off")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device
        self.on = False
    
    def turn_on(self):
        self.device.turn_on()
        self.on = True

    def turn_off(self):
        self.device.turn_off()
        self.on = False

if __name__ == '__main__':
    light_bulb = LightBulb()
    switch = Switch(light_bulb)
    switch.turn_on()    # Output: Switch light on
    print(f"{light_bulb.__class__.__name__} is {'on' if switch.on else 'off'}")   # Output: Light is on
    switch.turn_off()   # Output: Switch light off
    print(f"{light_bulb.__class__.__name__} is {'on' if switch.on else 'off'}")   # Output: Light is off

    fan = Fan()
    switch = Switch(fan)
    switch.turn_on()    # Output: Switch fan on
    print(f"{fan.__class__.__name__} is {'on' if switch.on else 'off'}") # Output: Fan is on
    switch.turn_off()   # Output: Switch fan off
    print(f"{fan.__class__.__name__} is {'on' if switch.on else 'off'}") # Output: Fan is off
