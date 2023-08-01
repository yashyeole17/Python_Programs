from abc import ABC, abstractmethod
class Computer:
    @abstractmethod
    def process(self):
        pass
com= Computer()
print(com.process())