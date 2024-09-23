from mpmath import mp
import re

#set digits after pi available to 100 and convert pi to a string data type
mp.dps = 100
pi = str(mp.pi)

#remove seperator (in this case dot)
pi = re.sub(r'(\.)','',pi)


#function to display the n-th digit of pi
n = int(input('Choose a number below 100: '))
if n <= 100:
      print(pi[n])
else:
     print('take it easy big boy!')