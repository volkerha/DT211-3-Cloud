squaresum = 0
sumofsquare = 0

#calc sum of squares and square of sum
for i in range(1, 101):
  squaresum += (i*i)
  sumofsquare += i
sumofsquare *= sumofsquare
#get the difference
dif = sumofsquare - squaresum
print(dif)