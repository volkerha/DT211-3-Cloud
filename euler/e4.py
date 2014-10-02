digit1 = 999
digit2 = 999
largestpal = 0 #always save the largest palindrome

#nested loop for 3digit product
while digit1 >= 1:
  while digit2 >= 1:
    #get string from int
    p1 = str(digit1 * digit2)
    #check string for palindrome by comparing first-last, etc.
    for i in range(0, (len(p1) - 1)):
      #no pal? go on
      if p1[i] != p1[len(p1)-i-1]:
        break
      #pal? save if larger than current
      elif i >= (len(p1)-1)/2:
        if largestpal < int(p1):
          largestpal = digit1 * digit2
          print (largestpal)
    digit2 -= 1
  digit1 -= 1
  digit2 = 999
print (largestpal)