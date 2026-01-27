class SecurePlant:
    """Class that represents a plant from a Garden"""

    def __init__(self, name: str) -> None:
        """
        Initialize a new plant instance.
        Args:
        :param self: The instance of the class used in this method.
        :param name: The name of the plant.
        """

        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        print(f"Plant created: {name}")
        """
        Args:
        - name (str): The name of the plant.
        - height (int): Height in centimeters.
        - age (int): Age in days.
        """
    def set_height(self, value: int) -> None:
        """
        Method for setting the height of plants

        :param self: The instance of the class used in this method.
        :param value: The height you want to set
        :type value: int
        """
        try:
            if value < 0:
                raise ValueError(f"Height {value}cm [REJECTED]")
            self.__height = value
            print(f"Height updated: {value}cm [OK]")
        except ValueError as e:
            print(f"Invalid operation attempted: {e}")
            print("Security: Negative height rejected")

    def set_age(self, value: int) -> None:
        """
        Method for establishing the age of plants

        :param self: The instance of the class used in this method
        :param value: The age you want to set
        :type value: int
        """
        try:
            if value < 0:
                raise ValueError(f"Age {value} days [REJECTED]")
            self.__age = value
            print(f"Age updated: {value} days [OK]")
        except ValueError as e:
            print(f"Invalid operation attempted: {e}")
            print("Security: Negative age rejected")

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
