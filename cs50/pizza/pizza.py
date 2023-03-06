import sys
import csv
from tabulate import tabulate


def main():

    check_args()

    table = []

    try:
        with open(sys.argv[1]) as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                table.append(line)

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, tablefmt="grid"))


def check_args():
    if too_many_args():
        sys.exit("Too many args")
    if too_few_args():
        sys.exit("Too few args")
    if not is_csv_file(sys.argv[1]):
        sys.exit("Not a csv file")


def too_many_args():
    return len(sys.argv) > 2


def is_csv_file(file_name):
    return file_name[-4:] == ".csv"


def too_few_args():
    return len(sys.argv) < 2


if __name__ == "__main__":
    main()
