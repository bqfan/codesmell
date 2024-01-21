# switch_dip.py
"""
Dependency inversion principle (DIP):
This principle states that high-level modules should not depend on low-level modules, but both should depend on abstractions. 

In this example, the Switch class depends directly on the LightBulb class, creating tight coupling.
"""
class LightBulb:
    def turn_on(self):
        print(f"Switch {light_bulb.__class__.__name__} on")

    def turn_off(self):
        print(f"Switch {light_bulb.__class__.__name__} off")

class Switch:
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb
        self.on = False

    def turn_on(self):
        self.on = True
        self.light_bulb.turn_on()

    def turn_off(self):
        self.on = False
        self.light_bulb.turn_off()

if __name__ == '__main__':
    light_bulb = LightBulb()
    switch = Switch(light_bulb)
    switch.turn_on()    # Output: Switch light on
    print(f"{light_bulb.__class__.__name__} is {'on' if switch.on else 'off'}")   # Output: Light is on

    switch.turn_off()   # Output: Switch light off
    print(f"{light_bulb.__class__.__name__} is {'on' if switch.on else 'off'}")   # Output: Light is off
