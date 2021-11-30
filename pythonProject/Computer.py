from abc import ABC, abstractmethod

class Computer (ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("it's running")

class Whiteboard:
    def write(self):
        print("writing")

class Programmer:
    def work(self, com):
        print("coding")
        com.process()

com1 = Laptop()
pro1 = Programmer()
white1 = Whiteboard()
pro1.work(com1)
pro1.work(white1)