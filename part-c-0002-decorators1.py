def division_control(func):
    def inner_func(x: int | float, y: int | float) -> (int | float | None):
        if y == 0:
            print("Zero division error! Be careful!")
            return None
        return func(x, y)
    return inner_func


@division_control
def divide(a: int | float, b: int | float):
    print(f"{a} / {b} = {a / b}")
    
divide(12, 4) # 12 / 4 = 3.0

divide(12.5, 5) # 12.5 / 5 = 2.5

divide(12.5, 0) # Zero division error! Be careful!
