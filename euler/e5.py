true = 0
counter = 1
div = 0

while true == 0:
  for i in range(1, 20):
    if (counter % i != 0):
      break
    if i == 20:
      div = i
      true = 1
      print(div)
      break
  counter += 1
print(div)