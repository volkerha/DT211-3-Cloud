true = 0
counter = 232500000

while counter < 232800000:
  for i in range(2, 19):
    #not divisible by 1-20? try next
    if (counter % i != 0):
      break
    #fully divisible? show number
    if i == 19:
      true = 1
      print(counter)
      break
  counter += 1