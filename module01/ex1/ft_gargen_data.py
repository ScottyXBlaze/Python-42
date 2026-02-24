class Plant:
    def __init__(self, name: str, length: str, age: str) -> None:
        self.name = name
        self.length = length
        self.age = age

    def display(self):
        print(f"{self.name}: {self.length}cm, {self.age} days old")


def main():
    rose = Plant("Rose", "13", "22")
    violet = Plant("Violet", "19", "12")
    dandelion = Plant("Dandelion", "8", "6")
    plants = [rose, violet, dandelion]
    for plant in plants:
        plant.display()


if __name__ == "__main__":
    main()
