

import multiprocessing


def write_file():
    with open("output.txt", "w") as f:
        f.write("This is a test file.\n")

def read_file():
    with open("output.txt", "r") as f:
        content = f.read()
        print(content)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)

    p1.start();
    p2.start();