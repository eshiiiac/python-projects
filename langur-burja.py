import random

print(
    '''
--------------------------------------
|        WELCOME TO LANGUR BURJA     |
|           BY: @ESHIIIAC            |
|   TYPE:                            |
|                                    |
|    PLAY    - TO PLAY               |
|    BAL     - CHECK BALANCE         |
|    RULES   - SEE RULES             |
|    EXIT    - EXIT GAME             |
--------------------------------------

'''
)

result = []
choices = ["jhanda","burja","itta","paan","hukum","chidi"]


def play():
    bal = 100
    print("-------------------------------------------------------------")

    print("please enter either jhanda, burja, itta, paan, hukum or chidi")

    print("-------------------------------------------------------------")

    userInput = input("Place bet on: ")

    print("-------------------------------------------------------------")

    userBet = int(input("Bet amount: Rs."))
    print("-------------------------------------------------------------")

    bal-=userBet

    result = []
    for x in choices:
        x = random.choice(choices)
        result.append(x)
    print(result)
    print("-------------------------------------------------------------")
    resCount = result.count(userInput)
    print("You got",resCount,userInput)
    print("-------------------------------------------------------------")

        
    if resCount == 1 or resCount == 0:
        print("better luck next time\n")
    elif resCount == 2:
        print("You won Rs.",userBet*resCount,"\n") 
    elif resCount == 3:
        print("You won Rs.",userBet*resCount,"\n") 
    elif resCount == 4:
        print("You won Rs.",userBet*resCount,"\n") 
    elif resCount == 5:
        print("You won Rs.",userBet*resCount,"\n")
    elif resCount == 6:
        print("You won Rs.",userBet*resCount,"\n")

def bal():
    return bal
    # print("Your balance is Rs.",bal,",use it wisely")

def rules():
    print(
    '''
    rules.txt
    '''
    )


while True:
    userCmd = input("What to do: ").lower()
    
    if(userCmd == "play"):
        play()
        continue

    elif(userCmd == "bal"):
        bal()
        continue

    elif(userCmd =="rules"):
        rules()
        continue

    elif(userCmd == "exit"):
        exit()