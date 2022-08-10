# Example of Factory Design Pattern
# The Pizza Factory

from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    def cook_time(self):
        pass


class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing Cheese Pizza")

    def cook_time(self):
        print("Cooking Cheese Pizza for 15 minutes")


class GreekPizza(Pizza):
    def prepare(self):
        print("Preparing Greek Pizza")

    def cook_time(self):
        print("Cooking Greek Pizza for 15 minutes")


class AllMeatPizza(Pizza):
    def prepare(self):
        print("Preparing All Meat Pizza")

    def cook_time(self):
        print("Cooking All Meat Pizza for 20 minutes")


class PizzaFactory(ABC):
    @abstractmethod
    def get_pizza(self) -> Pizza:
        pass


class CheesePizzaFactory(PizzaFactory):
    def get_pizza(self) -> Pizza:
        return CheesePizza()


class GreekPizzaFactory(PizzaFactory):
    def get_pizza(self) -> Pizza:
        return GreekPizza()


class AllMeatPizzaFactory(PizzaFactory):
    def get_pizza(self) -> Pizza:
        return AllMeatPizza()


def get_pizza_factory() -> PizzaFactory:
    pizza_factory = {
        "cheese": CheesePizzaFactory(),
        "greek": GreekPizzaFactory(),
        "allmeat": AllMeatPizzaFactory()
    }

    while True:
        pizza_type = input("Enter pizza type (cheese/greek/allmeat): ")
        if pizza_type in pizza_factory:
            return pizza_factory[pizza_type]
        else:
            print("Invalid pizza type")


def main():
    pizza_factory = get_pizza_factory()

    pizza = pizza_factory.get_pizza()
    pizza.prepare()
    pizza.cook_time()


if __name__ == "__main__":
    main()
