path_1 = "passwords.txt"
path_2 = "simple.txt"
path_3 = "output.txt"


def read_file_content(path):
    with open(path_1, "r") as first:
        return first.read()
    
    with open(path_2, "r") as second:
        return second.read()

    with open(path_3, "r+") as c:
        c.write(first + '\n')
        c.write(second + '\n')
        c.seek(0)
        c.read()

read_file_content(path_1)

