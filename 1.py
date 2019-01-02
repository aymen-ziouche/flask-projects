#db

db_username = "admin"
db_password = "123456"

user = None
password = None


while user != db_username or password != db_password :
    user = input("Enter Your Name : ")
    password = input("Enter Your Password : ")
    print("Username or password incorrect")
    print("--------------------")

print("Welcome To The Admin Panel")

