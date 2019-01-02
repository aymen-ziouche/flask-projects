import os

path = "simple.txt"
 
with open(path, "w") as fw:
    fw.write(input("Type whatever you want here: "))
    
 
 
with open(path, "a") as fa:
    while True:
        command = input("Append to the file or type 'exit' to exit: ")
        if command == "exit":
            break

        fa.write(command + "\n")

        print(command, "has been wrote to the file")
 
 
print("\n\nPrinting the complete file content:\n\n-------------------")
with open(path, "r") as fr:
    print(fr.read())
 
print("-----------------\n\nExiting...")
