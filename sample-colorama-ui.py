from colorama import init, Fore, Style
import time

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "\n=== PRIME GENERATOR ===\n")

number = int(input(Fore.YELLOW + "Enter starting number: "))
limit = int(input(Fore.YELLOW + "How many primes to generate: "))


def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def getNextPrime(number, limit):
    primeList = []
    
    while len(primeList) < limit:
        if isPrime(number):
            primeList.append(number)
        number += 1
    
    return primeList


print(Fore.MAGENTA + "\nCalculating primes", end="", flush=True)

for _ in range(3):
    time.sleep(0.4)
    print(Fore.MAGENTA + ".", end="", flush=True)

print("\n")

primes = getNextPrime(number, limit)

print(Fore.GREEN + Style.BRIGHT + "Prime numbers found:\n")

for p in primes:
    print(Fore.GREEN + f"  • {p}")

print(Fore.CYAN + "\nDone.\n")