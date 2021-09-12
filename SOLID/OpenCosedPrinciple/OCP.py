# Applications should be open to development but closed to change. Whenever we want to create a new class, we want to create this class comfortably. OOP already supports extensibility. However, it is necessary to establish the architecture in the classes created during this expansion so that no modification is required. -For example, let's think of a simple coffeshop application, in this application I have a coffe class and an enum to hold the coffee types. Every time a new type of coffee comes up, we add the type of coffee to the enum. In the Coffe class, the fee is calculated according to the unit price and amount of the coffee consumed according to the types of coffee related to if-else structures. However, the architecture in this scenario is contrary to this principle. If we want to follow this principle, we should define a method in an abstract class and use this method by overriding it in the classroom we will open for each coffee. In this way, I will not make a change in my existing classes for every coffee. With the help of the abstract class, we have kept our lower classes closed to change by setting rules.


import abc

class Coffee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetTotalPrice(self, amount):
        pass


class Latte(Coffee):
    def GetTotalPrice(self, amount):
        return amount * 4.50

class Mocha(Coffee):
    def GetTotalPrice(self, amount):
        return amount * 6.25

class FilterCoffee(Coffee):
    def GetTotalPrice(self, amount):
        return amount * 5.0
