sum = 0
m1 = 3
m2 = 5
const1 = 3
const2 = 5

counter = 1

while(counter < 1000):
  if (counter % const1 == 0 or counter % const2 == 0):
    sum += counter
  counter += 1
print(sum)
  
  