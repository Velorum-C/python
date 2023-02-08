def main():
    result = convert(input("What time is it? "))
    if result <= 8 and result >= 7:
        print("Breakfast time")
    elif result <= 13 and result >= 12:
        print("Lunch time")
    if result <= 19 and result >= 18:
        print("Dinner time")


def convert(time):
    hour = float(time.split(":")[0])
    minute = float(time.split(":")[1]) / 60
    return hour + minute


if __name__ == "__main__":
    main()
