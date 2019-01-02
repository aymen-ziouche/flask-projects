import random
import time
 
WORDLIST_FILENAME = "passwords.txt"
 
def load_words ():
    with open(WORDLIST_FILENAME, 'r') as words_file:
        return words_file.readlines()
 
 
words_list = [word.strip() for word in load_words()]
 
name = input("What is your name? ")
 
print( "Hello",  name, "Time to play hangman!\n")
print ("Start guessing...")
time.sleep(0.5)
 
word = random.choice(words_list)
guesses = ''
 
turns = 10
 
while turns > 0:        
 
    failed = 0            
 
    for char in word:      
        if char in guesses:    
            print (char,  )  
        else:
            print ("_",     )
            failed += 1    
 
    if failed == 0:        
        print ("You won")
        break              
 
    guess = input("\nguess a character:")
 
    guesses += guess                    
 
    if guess not in word:  
 
        turns -= 1        
        print ("Wrong\nYou have", + turns, 'more guesses' )
 
        if turns == 0:          
            print("You Lost :(\nThe word was:", word)