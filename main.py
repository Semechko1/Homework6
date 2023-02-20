result = []


def divider(a, b):
    if a < b:
        raise ValueError("A < B")
    if b > 100:
        raise IndexError
    return a / b


data = {10: 2, 2: 5, tuple("123"): 4, 18: 0, tuple([]): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
print(result)
