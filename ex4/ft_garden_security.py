class SecurePlant:
    """Class that represents a plant from a Garden"""

    def __init__(self, name: str) -> None:
        """
        Initialize a new plant instance.

        :param self: The instance of the class used in this method.
        :param name: The name of the plant.
        :type name: str
        """

        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        print(f"Plant created: {name}")

    def set_height(self, value: int) -> None:
        """
        Method for setting the height of plants

        :param self: The instance of the class used in this method.
        :param value: The height you want to set
        :type value: int
        """
        if value < 0:
            print(f"Invalid operation attempted: Height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """
        Method for establishing the age of plants

        :param self: The instance of the class used in this method
        :param value: The age you want to set
        :type value: int
        """

        if value < 0:
            print(f"Invalid operation attempted: Age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]")

    def get_info(self) -> None:
        """Display the plant's information."""
        print(f"Current plant: {self.name} ({self.__height}cm, "
              f"{self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    print("")
    rose.get_info()
