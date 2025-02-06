sales: dict[str, int] = {}

sales["TV"] = 17
sales["Radio"] = 12
sales["Smart Phone"] = 45

print(f"Sales dictionary: {sales}") # Sales dictionary: {'TV': 17, 'Radio': 12, 'Smart Phone': 45}

for key, value in sales.items():
    print(f"{key} -> {value}")

# TV -> 17
# Radio -> 12
# Smart Phone -> 45
