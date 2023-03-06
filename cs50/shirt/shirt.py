import sys
from PIL import Image
from PIL import ImageOps


def main():
    check_args(3)

    shirt_image = Image.open("shirt.png")
    size = shirt_image.size

    image = Image.open(sys.argv[1])
    image = ImageOps.fit(image, size)

    image.paste(shirt_image, mask=shirt_image)
    image.save(sys.argv[2])

    shirt_image.close()
    image.close()


def check_args(num_args):
    if too_few_args(num_args):
        sys.exit("Not enough args")
    if too_many_args(num_args):
        sys.exit("Too many args")
    if too_many_args(num_args):
        sys.exit("Not enough args")
    if incorrect_input(sys.argv[1]):
        sys.exit("Please input image file")
    if incorrect_output(sys.argv[1], sys.argv[2]):
        sys.exit("Please output to same file type")


def too_few_args(num_expected):
    return len(sys.argv) < num_expected


def too_many_args(num_expected):
    return len(sys.argv) > num_expected


def incorrect_input(file):
    if file[-5:] == ".jpeg":
        return False
    if file[-4:] in [".jpg", ".png"]:
        return False
    return True


def incorrect_output(file_in, file_out):
    return not file_in.split(".")[-1] == file_out.split(".")[-1]


if __name__ == "__main__":
    main()
