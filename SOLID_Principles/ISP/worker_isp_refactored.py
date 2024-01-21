# worker_isp_refactored.py
"""
Interface segregation principle (ISP):
This principle states that clients should not be forced to depend on interfaces that they do not use.

To comply with the ISP principle, we can seperate abstract class Worker to abstract classes Workable and Eatable
and make OfficeWorker a multiple inheritance to classes Workable, Eatable.
"""
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class OfficeWorker(Workable, Eatable):
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
