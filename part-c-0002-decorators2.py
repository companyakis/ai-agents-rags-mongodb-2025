def age_control(func):
    def inner_func(name: str, age: int) -> str:
        if age < 18:
            print("Voters must be over 18!")
            return f"{name} can vote!"
        return func(name, age)
    return inner_func


@age_control
def can_vote(name: str, age: int):
    print(f"Welcome voter {name}!")
    
can_vote("Ayhan", 23) # Welcome voter Ayhan!

can_vote("Hakan", 47) # Welcome voter Hakan!

can_vote("Begüm", 17) # Voters must be over 18!
