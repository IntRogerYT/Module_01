class Plant:
    """Class that represents a plant from a Garden"""

    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initialize a new plant instance.

        :param self: The class instance used int this method.
        :param name: The name of the plant.
        :type name: str
        :param height: The height of the plant (in cm).
        :type height: int
        :param age: The age of the plant (in days).
        :type age: int
        """
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def get_info(self) -> None:
        """Display the plant's information."""
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days")

    def grow(self) -> None:
        """Grow the plant 1 centimeter."""
        self.height += 1.0

    def ft_age(self) -> None:
        """Add one day to the age of the plant."""
        self.age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    for i in range(len(plants)):
        print("Created:", end=" ")
        plants[i].get_info()
