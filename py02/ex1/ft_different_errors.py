#!/usr/bin/env python3


def garden_operations(exception: str) -> None:
    if exception == "ValueError":
        i = int("abc")
        print(i)
    elif exception == "ZeroDivisionError":
        n = 1 / 0
        print(n)
    elif exception == "FileNotFoundError":
        name = "missing.txt"
        try:
            files = open(name)
            files.close()
        except FileNotFoundError:
            raise FileNotFoundError(f"No such file '{name}'")
    elif exception == "KeyError":
        plans = {"plants": "rose", "numbers": 1}
        i = plans["missing_plant"]
        print(i)
    else:
        print(f"Invalid parameters {exception}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    try:
        print("\nTesting ValueError...")
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        print("\nTesting ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    try:
        print("\nTesting FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    try:
        print("\nTesting KeyError...")
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: {str(e)}")

    print("\nTesting multiple errors together...")
    try:
        n = 1 / int("Honey")
        print(n)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
