import random
print(" ------------------------------ ")
print(" | WELCOME TO ROLL THE DICE!! | ")
print(" ------------------------------ ")

userDice = random.randint(1,6)
botDice = random.randint(1,6)

userCmd = input("type 'roll' to roll da dice: ").lower()


if(userCmd == ""):
    print("user entered:NOTHINGGG!!???")
    print("user is a DUMBF*CK\nDIDNT I TOLDYA TO TYPE 'ROLL'??\nNI**A DONT PLAY W ME")

elif(userCmd == "roll"):
    print("Bot Rolled...")
    print("Bot got:", botDice)

    print("You Rolled...")
    print("You got:", userDice)

    if(userDice == botDice):
        print("It's a tie")

    elif(userDice >= botDice):
        print("User Wins, GET A LIFE MAN, FR!")

    elif(userDice <= botDice):
        print("Bot wins, AHAHAHAHAHAH LOSER, BITCH GETA LIFE, FR")