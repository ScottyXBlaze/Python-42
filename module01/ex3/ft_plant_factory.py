class Plant:
    plants = 0
    def __init__(self, name: str, height: int, age: int) -> None:
        Plant.plants += 1
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Plant("Rose", 25, 30)
    Plant("Oak", 200, 365)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)
    Plant("Fern", 15, 120)
    print(f"\nTotal plants created: {Plant.plants}")
