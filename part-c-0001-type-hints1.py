def montly_sales_total(month: str, week1: int, week2: int, week3: int, week4: int) -> str: 
    
    return f"Month: {month} and total sales: {week1 + week2 + week3 + week4}"


january_total_sales = montly_sales_total("January", 25000, 18000, 42000, 17000)

print(january_total_sales) # Month: January and total sales: 102000
