items = {"apple": 7.5}

cost = 0

while True:
    try:
        selection = input("Item: ")

    except EOFError:
        print()
        exit(0)
    else:
        if selection in items:
            cost += items[selection]
            print(f"${cost}")
