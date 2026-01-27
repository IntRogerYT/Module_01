class Plant:
    """Class that represents a plant from a Garden"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant instance with 3 parameters"""

        self.name: str = name
        self.height: int = height
        self.age: int = age
        """
        Args:
        - name (str): The name of the plant.
        - height (int): Height in centimeters.
        - age (int): Age in days.
        """

    def get_info(self) -> None:
        """Display the plant's information."""
        print(f"{self.name} ({self.height}cm, {self.age} days)")

    def grow(self) -> None:
        """Grow the plant 1 centimeter."""
        self.height += 1

    def ft_age(self) -> None:
        """Add one day to the age of the plant."""
        self.age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    total_plants = len(plants)
    for i in range(0, total_plants):
        print("Created:", end=" ")
        plants[i].get_info()
    print(f"\nTotal plants created: {total_plants}")
