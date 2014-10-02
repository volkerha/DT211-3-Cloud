goal = 1000

a = 1
b = 2

#loop to 1000 tops, as we will be looking for a smaller number
while b < 1000:
  #a must always be less than b -> pythagoran triplet rule
  while a < b:
    cp = (a*a) + (b*b)
    #calc c according to pythagoran triplet rule
    c = cp**(0.5)
    #abc product is 1000? finish
    if (a + b + c) == goal:
      print(a)
      print(b)
      print(c)
      break
    a += 1
  b += 1
  a = 1