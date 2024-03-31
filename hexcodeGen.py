#hexcode generator
import random
import string

print(
    '''
----------------------------------------
| TYPE GEN TO GENERATE HEX COLOR CODES |
----------------------------------------
    '''
)
     
num = []     
char = []    
 
def genNum():
        for x in range(0,10):
            num.append(x)
        print(num)

def genChar():
     for a in range(0,10):
          a = random.choice(string.ascii_letters)
          char.append(a)
     print(char)

def generate():
     genChar()
     genNum()
     

while True:
    userInput = input("-> ").lower()

    if(userInput == "gen"):
        generate()
        code = char + num
        print(code)

    elif(userInput == "exit"):
        exit()

