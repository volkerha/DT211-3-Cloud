def isPrime(num):
  if(num == 2):
    return 1
  elif(num <= 1):
    return 0
  else:
    for i in range(2, (num+2)/2):
      if(num % i == 0):
        return 0
  return 1


primeSum = 0
limit = 2000000
counter = 0

for i in range(1, limit):
  if(isPrime(i) == 1):
    primeSum += i
  counter += 1
print(primeSum)
