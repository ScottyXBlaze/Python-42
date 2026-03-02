class Plant:
    def __init__(self, name: str, length: int, age: int) -> None:
        self.name = name
        self.length = length
        self.ages = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.length}cm, {self.ages} days old")

    def grow(self) -> None:
        self.length += 1

    def age(self) -> None:
        self.ages += 1


if __name__ == "__main__":
    day = 1
    rose = Plant("Rose", 25, 30)
    print(f"=== Day {day} ===")
    rose.get_info()
    while day < 7:
        rose.grow()
        rose.age()
        day += 1
    print(f"=== Day {day} ===")
    rose.get_info()
    print(f"Growth this week: +{day - 1}cm")

