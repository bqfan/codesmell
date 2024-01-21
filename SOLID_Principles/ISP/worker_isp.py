# worker_isp.py
"""
Interface segregation principle (ISP):
This principle states that clients should not be forced to depend on interfaces that they do not use.
 
The code violates the ISP as if we try to create a OfficeWorker class using Worker class
but an office worker doesn't have to eat in the office.
"""
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class OfficeWorker(Worker):
    def work(self):
        print("Working in the office")

    def eat(self):
        print("Eating in the office")

if __name__ == '__main__':
    office_worker = OfficeWorker()
    # work
    office_worker.work()    # Output: Working in the office
    # eat
    office_worker.eat()     # Output: Eating in the office
