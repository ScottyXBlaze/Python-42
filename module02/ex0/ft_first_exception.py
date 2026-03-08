def check_temperature(temp_str: str) -> int:
    try:
        temperature = int(temp_str)
    except TypeError:
        print("Temperature must be an integer")
        raise
    except ValueError:
        print("Temperature must be a valid integer")
        raise
    except Exception as e:
        print("Unknown error:", e)
    
    finally:
        pass
    return 0
