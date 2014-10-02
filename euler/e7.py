primeCount = 0
prime = 2
loopCount = 2

#check if numer is prime
def isPrime(p):
  for i in range(2, p):
    if p % i == 0:
      return 0
  return 1

#loop until the 10001st prime number
while primeCount < 10001:
  #prime? increse primecount
  if isPrime(loopCount) == 1:
    primeCount += 1
    prime = loopCount
  loopCount += 1

#last prime number
print(prime)
  