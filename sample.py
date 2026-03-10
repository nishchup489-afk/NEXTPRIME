number = int(input("Enter your number:  "))
limit = int(input("Enter your limit:  "))

def isPrime(n):
    if n < 2:
        return "need bigger than 2"
    
    for i in range(2 , int(n ** 0.5) + 1):
        if n%i == 0:
            return False
    return True
    
def getNextPrime(number , limit):
    primeList = []
    count = 0
    while count < limit:
        if isPrime(number):
            primeList.append(number)
            count+= 1
        number+=1

    return primeList

print(getNextPrime(number, limit))
    
