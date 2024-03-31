import random


print(
    '''
    -----------------------------------
    | WELCOME TO ROCK PAPER SCISSOR!! |
    -----------------------------------
    '''
)
while True:
    cChoice =random.choice(['rock', 'paper', 'scissor'])
    userChoice= input("Enter your choice: ").lower()
    print(" ----------------------------------- ")
    print("Computer's Choice:--",cChoice)
    print(" ----------------------------------- ")
    print( "Your Choice:--------",userChoice)
    print(" ----------------------------------- ")
    
    if(userChoice == cChoice):
        print(" | Its a tie |")
        print(" ----------------------------------- ")
        continue

    elif(userChoice=="rock" and cChoice=="scissor" ):
        print("| You win |")
        print(" ----------------------------------- ")
        continue

    elif(userChoice=="rock" and cChoice=="paper"):
        print("| computer wins |")
        print(" ----------------------------------- ")
        continue

    elif(userChoice=="paper" and cChoice=="scissor"):
        print("| computer wins |")
        print(" ----------------------------------- ")
        continue

    elif(userChoice=="paper" and cChoice=="rock"):
        print("| You win |")
        print(" ----------------------------------- ")
        continue

    elif(userChoice=="scissor" and cChoice=="rock"):
        print("| computer wins |")
        print(" ----------------------------------- ")
        continue

    elif(userChoice=="scissor" and cChoice=="paper"):
        print("| You win |")
        print(" ----------------------------------- ")
        continue
    