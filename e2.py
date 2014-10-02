fib1 = 1
fib2 = 2
tmp = 2
sum = 0

while fib2 < 4000000:
  if fib2 % 2 == 0:
    sum += fib2
  tmp = fib2
  fib2 += fib1
  fib1 = tmp
print(sum)
