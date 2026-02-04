class Plant:
    """Class that represents a plant from a Garden"""

    def __init__(self, name: str, height: int, age: int) -> None:
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
        self.height: int = height
        self.age: int = age

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
