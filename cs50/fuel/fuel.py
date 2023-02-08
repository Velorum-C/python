while True:
    result = input("Fraction: ").split("/")
    try:
        x = int(result[0])
        y = int(result[1])
    except ValueError:
        print("Please type valid integers")
    else:
        if x > y or y == 0:
            continue
        break

if x <= 0.01 * y:
    output = "E"
elif x >= 0.99 * y:
    output = "F"
else:
    output = str(round(100 * x / y)) + "%"
print(output)
