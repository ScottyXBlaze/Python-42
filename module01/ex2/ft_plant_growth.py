class Plant:
    def __init__(self, name: str, length: int, age: int) -> None:
        self.name = name
        self.length = length
        self.age = age

    def display(self):
        print(f"{self.name}: {self.length}cm, {self.age} days old")

    def grow(self):
        self.length += 1

    def ages(self):
        self.age += 1

    def get_info(self) -> int:
        return self.length


def main():
    rose = Plant("Rose", 14, 31)
    current_length = rose.get_info()
    day = 1
    print(f"=== Day {day} ===")
    rose.display()
    while day < 7:
        rose.ages()
        rose.grow()
        day += 1
    print(f"=== Day {day} ===")
    rose.display()
    print(f"Growth this week: +{rose.get_info() - current_length}cm")


if __name__ == "__main__":
    main()
