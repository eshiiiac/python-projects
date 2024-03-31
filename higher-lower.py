import random

r1= int(input("enter the starting range: "))
r2= int(input("enter the ending range: "))

botNum = random.randint(r1,r2)
print("the range is from", r1, "to", r2 ,"...Good Luck!")



while True:    
    userNum =  int(input("Guess the num: ")) 
    if(userNum<r1 or userNum>r2 or userNum==0):
        print("BItch enter the num between range", r1 ,"and", r2)
        
    if(userNum == botNum):
        print("Good job Lil Ni**a! you won!!")
        break 

    elif(userNum<botNum):
        print("You're close Lil Ni**a, but your num is slightly smaller")
        continue

    elif(userNum > botNum):
        print("You're close Lil Ni**a, but your num is slightly larger")
        continue  
