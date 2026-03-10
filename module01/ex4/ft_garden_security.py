class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            self.__height = 0
        else:
            self.__height = height
        if age < 0:
            print(f"Invalid operation attempted: {age} days [REJECTED]")
            print("Security: Negative age rejected")
            self.__age = 0
        else:
            self.__age = age
        print(f"Plant created: {self.__name}")

    def get_info(self) -> None:
        print(
            "Current plant:",
            f"{self.__name} ({self.__height}cm, {self.__age} days)",
            sep=" "
        )

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
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
