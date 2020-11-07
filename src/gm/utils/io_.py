import os


def read_input_file(*args, **kwargs):
    print("read_input_file func is under construction...")


def write_output_file(*args, **kwargs):
    print("write_output_file is under construction...")


def write_txt(lines, filename):
    with open(filename, "w", encoding="utf-8") as txtfile:
        for line in lines:
            txtfile.write(line + os.linesep)
