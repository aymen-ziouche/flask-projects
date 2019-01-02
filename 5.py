numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_odd(number):
    return number % 2 != 0

number = input("Enter the number: ")


if is_odd(int(number)):
    print(number, "is odd")
else:
    print(number, "is even")
