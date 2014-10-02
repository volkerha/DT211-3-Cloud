fib1 = 1
fib2 = 2
tmp = 2
sum = 0

while fib2 < 4000000:
  #even fib? add to sum
  if fib2 % 2 == 0:
    sum += fib2
  #swap fib to calc next fib
  tmp = fib2
  fib2 += fib1
  fib1 = tmp
print(sum)
