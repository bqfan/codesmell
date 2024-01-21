# file_manager_srp.py
"""
Single responsibility principle (SRP):
This principle states that a class or module should have one and only one reason to change.

class FileManager violates the SRP principle because it has too many responsibilities
"""
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

if __name__ == '__main__':
    ## read
    file = FileManager("./file_manager_srp_refactored.py")
    print(file.read())  # Output: content offile file_manager_srp_refactored.py
    ## write
    file = FileManager("./hello")
    file.write("Hello World!")  # file hello created
    print(file.read())  # Output: Hello World!

    ## compress
    file.compress() # file hello.zip created
    ## decompress
    file.decompress()   # file hello.zip unziped
    print(file.read())  # Output: Hello World!
