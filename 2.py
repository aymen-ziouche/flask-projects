file2 = open("passwords.txt", "r")

data = file2.read()

for i in data:
        print(i, end ="")

        