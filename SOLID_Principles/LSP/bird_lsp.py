# bird_lsp.py
"""
Liskov substitution principle (LSP):
This principle states that subtypes should be substitutable for their base types.

Bird class violates the LSP principle because if we create a subclass that has a different implementation of
the fly method, it may cause unexpected behaviours when passed into a method that expects an object of the Bird class.
"""
class Bird:
    def fly(self):
        print(f"{self.__class__.__name__} can fly")

class Penguin(Bird):
    def fly(self):
        raise Exception(f"{self.__class__.__name__} can't fly")

if __name__ == '__main__':
    def make_bird_fly(bird):
        bird.fly()

    bird = Bird()
    make_bird_fly(bird)  # Output: Bird can fly

    penguin = Penguin()
    make_bird_fly(penguin)  # Output: An exception is raised
