primeCount = 0
prime = 2
loopCount = 2

def isPrime(p):
  for i in range(2, p):
    if p % i == 0:
      return 0
  return 1

while primeCount < 10001:
  if isPrime(loopCount) == 1:
    primeCount += 1
    prime = loopCount
  loopCount += 1

print(prime)
  