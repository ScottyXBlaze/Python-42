#!/usr/bin/env python3


class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant_name: str = "tomato") -> None:
        self.plant_name = plant_name
        self.message = f"The {self.plant_name} plant is wilting!"

    def __str__(self) -> str:
        return self.message


class WaterError(GardenError):
    def __str__(self) -> str:
        return "Not enough water in the tank!"


def test_moisture(moisture: int) -> None:
    if moisture < 1:
        raise PlantError("tomato")
    print("Plant OK!")


def test_water(water: int) -> None:
    if water < 1:
        raise WaterError()
    print("Water OK!")


def test_errors() -> None:
    try:
        print("\nTesting PlantError...")
        test_moisture(0)
    except PlantError as e:
        print(f"Caught PlantError: {str(e)}")

    try:
        print("\nTesting WaterError...")
        test_water(0)
    except WaterError as e:
        print(f"Caught WaterError: {str(e)}")

    try:
        exceptions: list[Exception] = []
        print("\nTesting all garden errors...")

        try:
            test_moisture(0)
        except PlantError as e:
            exceptions += [e]
        try:
            test_water(0)
        except WaterError as e:
            exceptions += [e]

        raise GardenError(*exceptions)
    except GardenError as e:
        for exception in e.args:
            print(f"Caught a garden error: {exception}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
