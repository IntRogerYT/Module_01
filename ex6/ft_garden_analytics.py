class Plant:
    """Class that represents a plant from a Garden."""
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.stats: Plant.Stats = Plant.Stats()

    class Stats:
        """Nested class that holds statistical data for a Plant."""

        def __init__(self) -> None:
            self.__grow_calls: int = 0
            self.__age_calls: int = 0
            self.__show_calls: int = 0

        def increment_grow(self) -> None:
            self.__grow_calls += 1

        def increment_age(self) -> None:
            self.__age_calls += 1

        def increment_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self.__grow_calls} grow, "
                f"{self.__age_calls} age, "
                f"{self.__show_calls} show"
            )

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def display_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age} days old"
        )
        self.stats.increment_show()


class Flower(Plant):
    """Class that represents a Flower."""

    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def grow(self, amount: float) -> None:
        self.height += amount
        self.stats.increment_grow()

    def age_plant(self, days: int) -> None:
        self.age += days
        self.stats.increment_age()

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age} days old"
        )
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")
        self.stats.increment_show()


class Tree(Plant):
    """Class that represents a Tree."""

    class TreeStats(Plant.Stats):
        """Extended stats that also tracks produce_shade() calls."""

        def __init__(self) -> None:
            super().__init__()
            self.__shade_calls: int = 0

        def increment_shade(self) -> None:
            self.__shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self.__shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self.stats: Tree.TreeStats = Tree.TreeStats()

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self.trunk_diameter * 40.0, 1)}cm long and "
            f"{round(self.trunk_diameter, 1)}cm wide."
        )
        self.stats.increment_shade()

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age} days old"
        )
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")
        self.stats.increment_show()


class Seed(Flower):
    """Class that represents a Seed (inherits from Flower)."""

    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self, seed_count: int = 0) -> None:
        super().bloom()
        self.seeds = seed_count

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age} days old"
        )
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")
        print(f" Seeds: {self.seeds}")
        self.stats.increment_show()


class Vegetable(Plant):
    """Class that represents a Vegetable."""

    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, days: int) -> None:
        self.age += days
        self.height += days * 2.1
        self.nutritional_value += days
        self.stats.increment_grow()

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age} days old"
        )
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")
        self.stats.increment_show()


def display_statistics(plant: Plant) -> None:
    """Display statistics for any kind of plant."""
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_a_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_a_year(400)}"
    )

    print()
    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print()
    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print()
    print("=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age_plant(20)
    sunflower.bloom(42)
    sunflower.show()
    display_statistics(sunflower)

    print()
    print("=== Anonymous")
    unknown: Plant = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()
