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
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class Plant:
    def __init__(self, name: str, water_amount: int, sun_level: int) -> None:
        self.name = name
        self.water_amount = water_amount
        self.sun_level = sun_level

    def add_water(self, amount: int) -> None:
        self.water_amount += amount

    def get_info(self) -> None:
        print(
            f"{self.name}: healthy "
            f"(water: {self.water_amount}, sun: {self.sun_level})"
        )


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []
        self.water_amount = 10
        self.tank_size = 10

    def add_plants(self, plants: list[Plant]) -> None:
        print("Adding plants to garden...")
        for plant in plants:
            try:
                if plant.name != "" and plant is not None:
                    self.plants += [plant]
                    print(f"Added {plant.name} successfully")
                else:
                    raise GardenError("plant name cannot be empty or None!")
            except GardenError as e:
                print(f"Error adding plant: {e}")

    def water_plants(self, amount: int) -> None:
        print("Watering plants...")
        print("Opening watering system")
        plant_amount = 0
        for _ in self.plants:
            plant_amount += 1
        try:
            consumption = plant_amount * amount
            if consumption == 0:
                raise WaterError("No water used")
            elif consumption > self.water_amount:
                raise WaterError("No enough water in tank")

            self.water_amount -= consumption
            for plant in self.plants:
                plant.add_water(amount)
                print(f"Watering {plant.name} - success")
        except GardenError as e:
            print(f"Error watering plants: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> None:
        if plant.water_amount > 10:
            raise GardenError(
                f"water level {plant.water_amount}" " is too high (max 10)"
            )
        elif plant.water_amount < 1:
            raise GardenError(
                f"water level {plant.water_amount}" " is too low (min 1)"
            )
        elif plant.sun_level > 12:
            raise GardenError(
                f"sunlight hours {plant.sun_level}" " is too high (max 12)"
            )
        elif plant.sun_level < 2:
            raise GardenError(
                f"sunlight hours {plant.sun_level}" " is too low (min 2)"
            )
        else:
            plant.get_info()

    def recovery_system(self):
        print("Testing error recovery...")
        try:
            if self.water_amount < self.tank_size:
                raise WaterError("not enough water in tank")
            print("Water is full")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
            print("Filling the tank with water...")
            self.water_amount = self.tank_size
            print("System recovered and continuing")

    def test_plant_checks(self) -> None:
        print("Checking plant health...")
        for plant in self.plants:
            try:
                self.check_plant_health(plant)
            except Exception as e:
                print(f"Error checking {plant.name}: {e}")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    garden = GardenManager()

    plants = [
        Plant("Tomato", 3, 8),
        Plant("Letuce", 14, 8),
        # Plant("Carrot", 9, 19),
        Plant("", 2, 11),
    ]
    garden.add_plants(plants)
    print()
    garden.water_plants(1)
    print()
    garden.test_plant_checks()
    print()
    garden.recovery_system()
    print()
    print("Garden management system test complete!")
