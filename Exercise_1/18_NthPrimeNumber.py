# 18. Write a python program to find the 100th prime number.

MAX_SIZE = 1000000
primes = list()
flag = False

def sieveOfEratosthenes():
    isPrime = list()
    for i in range(MAX_SIZE):
        isPrime.append(True)

    i = 2
    while i * i < MAX_SIZE:
        if(isPrime[i]):
            j = i * i
            while j < MAX_SIZE:
                isPrime[j] = False
                j += i
        i += 1

    for i in range(2, MAX_SIZE):
        if isPrime[i]:
            primes.append(i)

def nthPrimeNumber(n):
    global flag
    if not flag:
        sieveOfEratosthenes()
        flag = True
    return primes[n-1]



# n = int(input("Enter a number: "))
n = 100
result = nthPrimeNumber(n)
print(result)
n = 897
result = nthPrimeNumber(n)
print(result)
n = 1048
result = nthPrimeNumber(n)
print(result)
n = 1
result = nthPrimeNumber(n)
print(result)