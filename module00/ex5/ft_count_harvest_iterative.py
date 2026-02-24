def ft_count_harvest_iterative():
    """Count down the days until harvest iteratively
    """
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
