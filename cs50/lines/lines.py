import sys

# test comment


def main():

    check_args()

    try:
        with open(sys.argv[1]) as file:
            no_blanks = [line for line in file.readlines() if not line.isspace()]
            no_comments = [line for line in no_blanks if line.strip()[0] != "#"]
            for line in no_comments:
                print(line.rstrip())
    except FileNotFoundError:
        sys.exit("File does not exist")

    counter = 0
    for _ in no_comments:
        counter += 1

    print(counter)


def check_args():
    if too_many_args():
        sys.exit("Too many args")
    if too_few_args():
        sys.exit("Too few args")
    if not is_py_file(sys.argv[1]):
        sys.exit("Not a Python file")


def too_many_args():
    return len(sys.argv) > 2


def is_py_file(file_name):
    return file_name[-3:] == ".py"


def too_few_args():
    return len(sys.argv) < 2


if __name__ == "__main__":
    main()
