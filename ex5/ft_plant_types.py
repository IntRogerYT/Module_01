class Plant:
    """Class that represents a plant from a Garden"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new plant instance.

        :param self: The instance of the class used in this method.
        :param name: The name of the plant.
        :type name: str
        :param height: The height of the plant.
        :type height: int
        :param age: The age of the plant.
        :type age: int
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """Subclass representing a flower-type plant"""
    def __init__(self, name: str, height: int, age: int, color: str):
        """
        Initialize a new flower type plant instance.

        :param self: The instance of the class used in this method.
        :param name: The name of the flower.
        :type name: str
        :param height: The height of the flower.
        :type height: int
        :param age: The age of the flower.
        :type age: int
        :param color: The color of the flower.
        :type color: str
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
        :param name: The name of the tree.
        :type name: str
        :param height: The height of the tree.
        :type height: int
        :param age: The age of the tree.
        :type age: int
        :param color: The color of the tree.
        :type color: str
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
        :param name: The name of the vegetable.
        :type name: str
        :param height: The height of the vegetable.
        :type height: int
        :param age: The age of the vegetable.
        :type age: int
        :param harvest_season: The harvest season of the vegetable.
        :type harvest_season: str
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        print(f"{name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")

    def nutritional_value(self):
        """Method for vegetable to see it's nutritional value"""
        print(f"{self.name} is rich in vitamin C")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer")
    tomato.nutritional_value()
