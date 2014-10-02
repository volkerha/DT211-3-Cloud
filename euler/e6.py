squaresum = 0
sumofsquare = 0

for i in range(1, 101):
  squaresum += (i*i)
  sumofsquare += i
sumofsquare *= sumofsquare
div = sumofsquare - squaresum
print(div)