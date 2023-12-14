import random

def isItPerfect(n):
    if n == 1 or n == 0:
        return False
    else:
        divNums = list[1]
    for i in range(2, n, 1):
        if n % i == 0:
            divNums.append(i)
    
    return sum(divNums) == n
    
def randGen(s, e, a):
    nums = list()
    for i in range(a):
        nums.append(random.randint(s, e))
    return nums
    
def CreateNum(text):
    while True:
        n = input(text)
        try:
            n = int(n)
            return n
        except ValueError:
            print('Helytelen értéket adott meg!')
#itt indul a fő program (main):
perfNums = list()
perfNumFreq = dict()
startMess= 'Kezdő érték: '
endMess = 'Végérték: '
amountMess = 'Értékek száma: '

start = CreateNum(startMess)
end = CreateNum(endMess)
amount = CreateNum(amountMess)

nums = randGen(start, end, amount)

for num in nums:
    if isItPerfect == num:
        perfNums.append(num)

for num in perfNums:
    if num in perfNumFreq.keys():
        perfNumFreq[num] += 1
    else:
        perfNumFreq[num] = 1

for key in perfNumFreq.keys():
    print(f'{key}: {perfNumFreq[key]}')

input('Press Enter to exit!')