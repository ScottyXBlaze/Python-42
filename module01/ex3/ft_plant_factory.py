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
    plants = [("Rose", 25, 30),
              ("Oak", 200, 365),
              ("Cactus", 5, 90),
              ("Sunflower", 80, 45),
              ("Fern", 15, 120)]

    garden = []
    count = 0
    for plant in plants:
        garden.append(Plant(*plant))
        count += 1

    for plant in garden:
        print(f"Created : {plant.name} ({plant.length}cm, {plant.age} days)")
    print(f"Total plants created : {count}")


if __name__ == "__main__":
    main()
