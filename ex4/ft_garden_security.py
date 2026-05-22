class SecurePlant:
    """Class that represents a plant from a Garden"""

    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initialize a new plant instance.

        :param self: The instance of the class used in this method.
        :param name: The name of the plant.
        :type name: str
        """

        self.name: str = name
        self.__height: float = height
        self.__age: int = age
        print(f"Plant created: {self.name}: {round(self.__height)}, "
              f"{self.__age} days old")

    def set_height(self, value: float) -> None:
        """
        Method for setting the height of plants

        :param self: The instance of the class used in this method.
        :param value: The height you want to set
        :type value: int
        """
        if value < 0.0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm")

    def set_age(self, value: int) -> None:
        """
        Method for establishing the age of plants

        :param self: The instance of the class used in this method
        :param value: The age you want to set
        :type value: int
        """

        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days")

    def get_info(self) -> None:
        """Display the plant's information."""
        print(f"Current state: {self.name}: {float(round(self.__height))}cm, "
              f"{self.__age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15.0, 10)
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-5.0)
    rose.set_age(-2)
    print()
    rose.get_info()
