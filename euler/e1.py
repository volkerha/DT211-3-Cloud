sum = 0
const1 = 3
const2 = 5

counter = 1

while(counter < 1000):
  #multiple of 3 or 5? add to sum
  if (counter % const1 == 0 or counter % const2 == 0):
    sum += counter
  counter += 1
print(sum)
  
  