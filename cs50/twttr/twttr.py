def main():
    result = input("Input: ")
    print(f"Output: {shorten(result)}")


def shorten(in_string):
    return in_string.translate({ord(i): None for i in "aeiouAEIOU"})


if __name__ == "__main__":
    main()
