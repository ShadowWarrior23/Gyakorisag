import random

def isItPerfect():
    pass
    
def randGen(s, e, a):
    nums = list()
    for i in range(a):
        nums.append(random.randint(s, e))
    return nums
    
def CreateNum(text):
    isCorrect = False
    while isCorrect:
        n = input(text)
        try:
            n = int(n)
            isCorrect = True
            return n
        except ValueError:
            print('Helytelen értéket adott meg!')

startMess= 'Kezdő érték: '
endMess = 'Végérték: '
amountMess = 'Értékek száma: '

start = CreateNum(startMess)
end = CreateNum(endMess)
amount = CreateNum(amountMess)

randGen(start, end, amount)
    
input('Press Enter to exit!')