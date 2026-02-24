def ft_water_reminder() -> None:
    """Check if a plant needs to be harvesed
    """
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
