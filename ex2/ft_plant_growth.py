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
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        """Grow the plant 1 centimeter."""
        self.height += 1

    def ft_age(self) -> None:
        """Add one day to the age of the plant."""
        self.age += 1


if __name__ == "__main__":
    Rose = Plant("Rose", 24, 29)
    for i in range(1, 8):
        Rose.ft_age()
        Rose.grow()
        if i == 1 or i == 7:
            print(f"=== Day {i} ===")
            Rose.get_info()
