class Plant:
    """Class that represents a plant from a Garden"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new plant instance.
        Args:
        :param self: The instance of the class used in this method.
        :param name: The name of the plant.
        :param height: The height of the plant.
        :param age: The age of the plant.
        """

        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """subclass representing a flower-type plant"""
    def __init__(self, name: str, height: int, age: int, color: str):
        """
        Initialize a new flower type plant instance.

        :param self: The instance of the class used in this method.
        :param name (str): The name of the flower.
        :param height (int): The height of the flower.
        :param age (int): The age of the flower.
        :param color (str): The color of the flower.
        """
        super().__init__(name, height, age)
        self.color: str = color
        print(f"{name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self):
        """method for making the flower bloom"""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """subclass representing a tree-type plant"""
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """
        Initialize a new tree-type plant instance.

        :param self: The instance of the class used in this method.
        :param name (str): The name of the tree.
        :param height (int): The height of the tree.
        :param age (int): The age of the tree.
        :param color (str): The color of the tree.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter
        print(f"{name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        """Method for the tree to produce shade."""
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    """subclass representing a vegetable-type plant"""
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        """
        Initialize a new vegetable-type plant instance.

        :param self: The instance of the class used in this method.
        :param name (str): The name of the vegetable.
        :param height (int): The height of the vegetable.
        :param age (int): The age of the vegetable.
        :param harvest_season (str): The harvest season of the vegetable.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        print(f"{name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")
