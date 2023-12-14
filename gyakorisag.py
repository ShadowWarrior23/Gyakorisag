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
    


amount = input('Értékek száma: ')

isCorrect = False
while not isCorrect:
    end = input("Végérték: ")
    try:
        end = int(end)
        isCorrect = True
    except ValueError:
        print('Helytelen értéket adott meg!')
    
input('Press Enter to exit!')