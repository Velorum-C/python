def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s.isalnum():
        return False

    if not s[0:1].isalpha():
        return False

    had_num = False
    for char in s:
        if had_num and char.isalpha():
            return False
        if char.isnumeric():
            if not had_num and char == '0':
                return False
            had_num = True

    return True


if __name__ == "__main__":
    main()
