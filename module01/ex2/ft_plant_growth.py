class Plant:
    def __init__(self, name: str, length: int, age: int) -> None:
        self.name: str = name
        self.length: int = length
        self.ages: int = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.length}cm, {self.ages} days old")

    def grow(self, n: int = 1) -> int:
        self.length += n
        return n

    def age(self) -> None:
        self.ages += 1


if __name__ == "__main__":
    day = 1
    total_growth = 0
    plants = [Plant("Rose", 25, 30), Plant("Violets", 10, 11)]
    rose = Plant("Rose", 25, 30)

    print(f"=== Day {day} ===")
    for plant in plants:
        plant.get_info()

    while day < 7:
        for plant in plants:
            total_growth += plant.grow()
            plant.age()
        day += 1

    print(f"=== Day {day} ===")
    for plant in plants:
        plant.get_info()

    print(f"Growth this week: +{total_growth}cm")
