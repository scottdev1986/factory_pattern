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
        return 10


class GreekPizza(Pizza):
    def prepare(self):
        print("Preparing Greek Pizza")

    def cook_time(self):
        return 20


class AllMeatPizza(Pizza):
    def prepare(self):
        print("Preparing All Meat Pizza")

    def cook_time(self):
        return 30


def main():
    pizza: str

    while True:
        pizza = input("Enter pizza type (cheese/greek/allmeat): ")
        if pizza in {"cheese", "greek", "allmeat"}:
            break
        else:
            print("Invalid pizza type")

    # Create a pizza object
    pizza_maker: Pizza

    if pizza == "cheese":
        pizza_maker = CheesePizza()
    elif pizza == "greek":
        pizza_maker = GreekPizza()
    else:
        pizza_maker = AllMeatPizza()

    # Prepare the pizza
    pizza_maker.prepare()
    # Cook the pizza
    print("Cooking time:", pizza_maker.cook_time(), "minutes")


if __name__ == "__main__":
    main()
