try:
    mph = int(input("Enter the Wind speed of your hurricane: "))
    if mph < 39:
        print("Below 39mph: Not a tropical storm or hurricane")
    elif mph <= 73:
        print("Tropical Storm")
    elif mph <= 95:
        print("Category 1 hurricane: Very dangerous winds will produce some damage")
    elif mph <= 110:
        print("Category 2 hurricane: Extremely dangerous winds will cause extensive damage")
    elif mph <= 129:
        print("Category 3 hurricane: Devastating damage will occur")
    elif mph <= 156:
        print("Category 4 hurricane: Catastrophic damage will occur")
    elif mph >= 157:
        print("Category 5 hurricane: Catastrophic damage; high devastation")
    print(mph, "mph")

except ValueError:
    print("Incorrect, please enter a valid number.")
