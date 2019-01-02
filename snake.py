snake = input ("Enter the name of the most deadliest snake in the world: ")
print ("")
print ("\nThe length of your message is" , len(snake))
print ("The most deadliest snake in the world is Black mamba: ")

if "mamba" in snake:
    print ("which is in your message")
elif "Mamba" in snake:
    print ("which is in your message")
else:
    print ("which is not in your message")

input ("Enter to exit")