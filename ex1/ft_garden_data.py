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

    def display_info(self) -> None:
        """Display the plant's information in an organized way."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Main function to manage and display plant data."""
    print("=== Garden Plant Registry ===")

    garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    for i in range(len(garden)):
        garden[i].display_info()


if __name__ == "__main__":
    main()
