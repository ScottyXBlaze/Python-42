class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height} [REJECTED]")
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


def main():
    print("=== Gargen Security System ===")
    rose = SecurePlant("Rose", 10, 11)
    print(f"Plant created: {rose.name}")
    rose.set_height(-900)
    print("")
    rose.set_age(3)
    print("")
    print(f"Current plant: Rose ({rose.get_height()}cm, {rose.get_age()})")


if __name__ == "__main__":
    main()
