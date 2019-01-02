from math import pi

#Radius = input("Enter the Radius : ")



def fib(number):
    previous, current = (0, 1)

    previous, current = current, previous


    for i in range(number):
        print(current)
        previous, current = current, (current + previous)
        
        #z = previous
        #previous = current
        #current = current + z
        
        
    #while number != 1 :
       # number = number - 1
       # result = result * number
        

(fib(6))
