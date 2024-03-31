# temperature converter

def toCelcius():
    cel = int(input("ENter temperature in Celcius: "))
    F = (1.8 * cel)+32
    print(F,"F")

def toFarenheit():
    far = int(input("ENter temperature in Farenheit: "))
    C = (far - 32)/1.8
    print(C,"Degree Celcius")
    
print(
    '''
------------------------------------------------
|      TYPE cel for converting to celcuis       |
|      TYPE far for converting to Farenheit     |
------------------------------------------------
    '''
)

while True:
    userInput = input("-> ").lower()

    if(userInput=="cel"):
        toCelcius()

    elif(userInput=="far"):
        toFarenheit()