class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        print(
            f"{self.name} (Flower):",
            f"{self.height}cm, {self.age} days, {self.color} color",
            sep=" "
        )


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"{self.name} provides",
            f"{self.trunk_diameter * 1.56:.0f} square meters of shade",
            sep=" "
              )

    def get_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm,",
              f"{self.age} days, {self.trunk_diameter}cm diameter",
              sep=" ")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def get_info(self) -> None:
        print(
            f"{self.name} (Vegetable): {self.height}cm,",
            f"{self.age} days, {self.harvest_season} harvest",
            sep=" "
        )
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Violets", 12, 22, "blue")
    ]
    for flower in flowers:
        print()
        flower.get_info()
        flower.bloom()

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Palm", 820, 2829, 32)
    ]
    for tree in trees:
        print()
        tree.get_info()
        tree.produce_shade()

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 12, 32, "spring", "potassium")
    ]
    for vegetable in vegetables:
        print()
        vegetable.get_info()
