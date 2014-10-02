digit1 = 999
digit2 = 999
largestpal = 0


while digit1 >= 1:
  while digit2 >= 1:
    p1 = str(digit1 * digit2)
    for i in range(0, (len(p1) - 1)):
      if p1[i] != p1[len(p1)-i-1]:
        break
      elif i >= (len(p1)-1)/2:
        if largestpal < int(p1):
          largestpal = digit1 * digit2
          print (largestpal)
    digit2 -= 1
  digit1 -= 1
  digit2 = 999
print (largestpal)