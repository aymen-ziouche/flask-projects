from random import randint 

print(4 * "\t","========>Ghost Game<========")

score = 0
while 1:
    ghost_door = randint(0, 3)
    print(3 *"\t","three doors ahead ==> ghost behind one of them")
    print(4 *"\t","choose which door to open")
    door= input("Enter One Door From 1 To 3 : ")
    door_num = int(door)
    if door_num not in range(0, 4):
        print("You kidding me? I said THREE doors ahead!")
        continue

    if door_num == ghost_door:
        print("Ghooost")
        break
    else:
        print("No Ghost , Good")
        print("You Enter The Next Room")
        score = score + 1 

print("Run Away Ghost Behind You")
print("Your Score Is : ", score)