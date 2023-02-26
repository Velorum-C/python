import string


def main():

    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):

    greeting = greeting.translate(str.maketrans("", "", string.punctuation))

    if greeting.split()[0].lower() == "hello":
        return "$0"

    if greeting[0].lower() == "h":
        return "$20"

    return "$100"


if __name__ == "__main__":
    main()
