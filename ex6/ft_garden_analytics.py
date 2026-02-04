class Plant:
    """Class that represents a plant from a garden"""
    def __init__(self, name: str, height: int) -> None:
        """
        Initialize a new plant instance.

        :param self: The instance of the class used in this method.
        :param name: The name of the plant.
        :param height: The height of the plant.
        """
        self._name: str = name
        self._height: int = height


class FloweringPlant(Plant):
    """subclass representing a flowering plant"""
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Initialize a new flowering plant instance.

        :param self: The instance of the class used in this method.
        :param name (str): The name of the flower.
        :param height (int): The height of the flower.
        :param color (str): The color of the flower.
        """
        super().__init__(name, height)
        self._color: str = color


class PrizeFlower(FloweringPlant):
    """subclass that represents a prize flower"""
    def __init(self, name: str, height: int,
               color: str, prize_points: int) -> None:
        """
        Initialize a new prize plant instance.

        :param self: The instance of the class used in this method.
        :param name: The name of the flower.
        :type name: str
        :param height: The height of the flower.
        :type height: int
        :param color: The color of the flower.
        :type color: str
        :param prize_points: The prize points of the plant.
        :type prize_points: int
        """
        super().__init__(name, height, color)
        self._prize_points = prize_points


class GardenManager:
    """Class that represents a garden manager"""
    def __init__(self, name: str) -> None:
        """
        Initialize a new garden manager instance.

        :param self: The instance of the class used in this method.
        :param name: The name of the garden manager.
        :type name: str
        """
        self.name: str = name
        self.gardens: list[Garden] = []

    def add_garden(self, name: str) -> None:
        """
        Add a garden to the garden manager

        :param self: The instance of the class used in this method.
        :param name: The name of the new garden.
        :type name: str
        """
        new_garden = Garden(name)
        self.gardens.append(new_garden)

    @staticmethod
    def create_garden_network(manager1: str, manager2: str) -> list:
        """
        Method to create a garden network

        :param manager1: The name of the first garden manager.
        :type manager1: str
        :param manager2: The name of the second garden manager.
        :type manager2: str
        :return: A list with the two garden managers instances.
        :rtype: list[manager1, manager2]
        """
        m1 = GardenManager(manager1)
        m2 = GardenManager(manager2)
        return [m1, m2]


class Garden(GardenManager):
    """Subclass that represents a garden"""
    def __init__(self, name: str) -> None:
        """
        Initialize a new garden instance.

        :param self: The instance of the class used in this method.
        :param name: The name of the garden.
        :type name: str
        """
        self.name = name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant to the garden

        :param self: The instance of the class used in this method.
        :param plant: the plant instance to add to the garden.
        :type plant: Plant
        """
        if isinstance(plant, Plant):
            self.plants.append(plant)
