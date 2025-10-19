from abc import ABC, abstractmethod

# class Worker(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Human (Worker):
#     def work(self):
#         return "Human working..."
#
#     def eat(self):
#         return "Human eating..."
#
#
# class Robot (Worker):
#         def work(self):
#             return "Robot working..."
#
#         def eat(self):
#             raise NotImplementedError ("Robots cant eat")
#

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

    def work_overtime(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorkable(Workable, Eatable):
    def work(self):
        return "Human working..."
    def eat(self):
        return "Human eating..."

class Robot(Workable):
    def work(self):
        return "Robot working..."