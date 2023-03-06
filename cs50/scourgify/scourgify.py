import sys
import csv


def main():

    check_args(3)

    try:
        csv_file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    try:
        csv_out = open(sys.argv[2], "a")
    except FileNotFoundError:
        sys.exit("File does not exist")

    students = []
    csv_reader = csv.DictReader(csv_file)
    csv_writer = csv.DictWriter(csv_out, fieldnames=["first", "last", "house"])

    for line in csv_reader:
        students.append(line)

    for student in students:
        house = student["house"]
        first = student["name"].split(",")[1].strip()
        last = student["name"].split(",")[0].strip()

        csv_writer.writerow({"first": first, "last": last, "house": house})


def check_args(num_args):
    if too_many_args(num_args):
        sys.exit("Too many args")
    if too_few_args(num_args):
        sys.exit("Too few args")
    if not is_csv_file(sys.argv[1]):
        sys.exit("Not a csv file")
    if not is_csv_file(sys.argv[2]):
        sys.exit("Not a csv file")


def too_many_args(num_args):
    return len(sys.argv) > num_args


def is_csv_file(file_name):
    return file_name[-4:] == ".csv"


def too_few_args(num_args):
    return len(sys.argv) < num_args


if __name__ == "__main__":
    main()
