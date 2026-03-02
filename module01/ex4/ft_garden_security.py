class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.__name}")

    def get_info(self) -> None:
        name = self.__name
        height = self.__height
        age = self.__age
        print(f"Current plant: {name} ({height}cm, {age} days)")

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    print("=== Gargen Security System ===")
    rose = SecurePlant("Rose", 10, 11)
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    print("")
    rose.get_info()
