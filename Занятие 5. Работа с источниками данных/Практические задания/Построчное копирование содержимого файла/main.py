INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r", encoding="utf-8") as input_file:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as output_file:
            for line in input_file:
                output_file.write(line.upper())

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as file:
        for current_line in file:
            print(current_line, end="")
