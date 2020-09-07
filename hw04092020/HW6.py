from itertools import count, cycle
 for i in count(14):
     if i > 30:
         break
     print(i)

 el = 0
 for letter in cycle(['hello']):
     if el > 20:
         break
     print(letter)
     el += 1
