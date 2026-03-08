def garden_operations() -> None:
    _ = int("abc")
    _ = 1 / 0
    file = open("none.txt", "r")
    file.close()
    dictionnary = {"name": "Kenny", "age": 10}
    print(dictionnary["height"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===", end="\n\n")
    print("Testing ValueError...")
    try:
        _ = int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        _ = 1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    name = "missing.txt"
    try:
        file = open(name, "r")
        print("File opened successfully")
        file.close()
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{name}'")

    plants = {"name": "Roses", "color": "red"}
    key = "missing_plant"
    print("\nTesting KeyError...")
    try:
        print(plants[key])
    except KeyError:
        print(f"Caught KeyError: '{key}'")

    print("\nTesting multiple errors together...")
    try:
        print(1 / 0)
    except Exception:
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
