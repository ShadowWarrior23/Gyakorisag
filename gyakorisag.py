import random

def isItPerfect():
    pass

def makeNum(n):
    try:
        n = int(n)
    except ValueError:
        n = None
    return n
    
def repInp():
    start = None
    while start == None:
        start = input("Kezdő érték: ")
        if makeNum(start):
            print(start)
        else:
            print('Helytelen értéket adott meg!')
    
def CreateNum():
    #isCorrect = False
    while True:          #isCorrect:
        n = input("Kérek egy számot: ")
        try:
            n = int(n)
            return n
        except ValueError:
            print('Helytelen értéket adott meg!')

amount = input('Értékek száma: ')


    
input('Press Enter to exit!')