def main():

    while True:
        input_fraction = input("Fraction: ")
        try:
            percentage = convert(input_fraction)
            break

        except Exception as e:
            continue

    print(gauge(percentage))


def convert(fraction):
    value = fraction.split("/")

    try:
        x = int(value[0])
        y = int(value[1])

    except ValueError as e:
        raise e

    if x > y:
        raise ValueError("Fraction must be less than one")

    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return round(100 * x / y)


def gauge(percentage):

    if percentage <= 1:
        return "E"

    if percentage >= 99:
        return "F"

    return str(percentage) + "%"


if __name__ == "__main__":
    main()
