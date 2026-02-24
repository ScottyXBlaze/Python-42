def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """Print inventory

    Args:
        seed_type (str): type of the seed/plant
        quantity (int): numbers of the seeds
        unit (str): units of the quantity used
    """
    seed_name = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{seed_name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
