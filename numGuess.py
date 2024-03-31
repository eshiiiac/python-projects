import random 
ranNum = random.randint(0,10)
print("Guess the number from 0 to 10 to win: ")
userInput = int(input(print("your answer: ")))

if userInput == ranNum:
    print("You Guessed it right!")
else:
    print("Wrong answer")
