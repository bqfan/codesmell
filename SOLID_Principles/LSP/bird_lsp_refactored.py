# bird_lsp_refactored
"""
Liskov substitution principle (LSP):
This principle states that subtypes should be substitutable for their base types.

To comply with the LSP principle, we can create an abstract Bird class and have specific bird classes
(e.g., Sparrow, Penguin, tec.) to extend it.
"""
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print(f"{self.__class__.__name__} can fly")

class Penguin(Bird):
    def fly(self):
        print(f"{self.__class__.__name__} can't fly")

if __name__ == '__main__':
    # Sparrow
    bird = Sparrow()
    bird.fly()  # Output: Sparrow can fly

    # Penguin
    bird = Penguin()
    bird.fly()  # Output: Penguin can't fly