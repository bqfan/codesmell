1. Single Responsibility Principle (SRP)
```
❯ python3
# file_manager_srp.py
>>> from SRP.file_manager_srp import FileManager
## read
>>> file = FileManager("./SRP/file_manager_srp_refactored.py")
>>> file.read()
## write
>>> file = FileManager("./hello")
>>> file.write("Hello World!")
## compress
>>> file.compress()
## decompress
>>> file.decompress()

# file_manager_srp_refactored.py

>>> from SRP.file_manager_srp import FileManager
## read
>>> file = FileManager("./SRP/file_manager_srp.py")
>>> file.read()
## write
>>> file = FileManager("./hello")
>>> file.write("Hello World!")

>>> from SRP.file_manager_srp_refactored import ZipFileManager
## compress
>>> file = ZipFileManager("./hello")
>>> file.compress()
## decompress
>>> file.decompress()
```
2. Open/Closed Principle (OCP)
```
# shapes_ocp.py
>>> from OCP.shapes_ocp import Shape
## rectangle
>>> rectangle = Shape("rectangle", width=2, height=4)
>>> shape.area()
8
## circle
>>> circle = Shape("circle", radius=4)
>>> circle.area()
50.26548245743669

# shapes_ocp_refactored.py
## rectangle
>>> from OCP.shapes_ocp_refactored import Rectangle
>>> rectangle = Rectangle(2, 4)
>>> rectangle.area()
8
## circle
>>> from OCP.shapes_ocp_refactored import Circle
>>> circle = Circle(4)
>>> circle.area()
50.26548245743669
```

3. Liskov Substitution Principle (LSP)
>>> from shapes_lsp import Square
>>> square = Square(5)
>>> vars(square)
{'width': 5, 'height': 5}

>>> square.width = 7
>>> vars(square)
{'width': 7, 'height': 7}

>>> square.height = 9
>>> vars(square)
{'width': 9, 'height': 9}