from itertools import permutations

chk_str = 'balloon'
Alist = ['fly','on', 'o', 'hot', 'ball', 'air']

def findstring(strchk, biglist):
   for i in range(2, len(biglist) + 1):
      for perm in permutations(biglist, i):
         if ''.join(perm) == strchk:
            return True
   return False

# Using the function
if(findstring(chk_str,Alist)):
   print("String can be formed.")
else:
   print("String can not be formed.")