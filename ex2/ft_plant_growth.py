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
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self) -> None:
        """Grow the plant 1 centimeter."""
        self.height += 0.8

    def ft_age(self) -> None:
        """Add one day to the age of the plant."""
        self.age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    Rose = Plant("Rose", 24.0, 29)
    growth = 0.0
    for i in range(1, 8):
        Rose.ft_age()
        Rose.grow()
        growth += 0.8
        print(f"=== Day {i} ===")
        Rose.get_info()
    print(f"Growth this week: {growth}cm")
