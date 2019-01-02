db_username = "admin"
db_password = "123456789"

password_lenght = len(db_password)

attempts = 4

user = None
password = None

def check_password_length(password, password_lenght):
    if len(password) < password_lenght:
        print("minimum password lenth is ", password_lenght)


def login(attempts, password_lenght):
    for attempt in range(1, attempts + 1):
        user = input("Enter Your Name : ")
        password = input("Enter Your Password : ")


        if user == db_username and password == db_password:
            print("Welcome To The Admin Panel")
            break
        elif user != db_username and password != db_password:
            print("both the username and password incorrect")
            check_password_length(password, password_lenght)
        elif user != db_username:
            print("username incorrect")
        else:
            print("password incorrect")
            check_password_length(password, password_lenght)


        print("attempt number : ", attempt)
        print("remaining : ", attempts - attempt)
        print("--------------------")

login(3, 10)
login(6, 5)

