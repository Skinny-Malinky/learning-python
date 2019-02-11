def findFib(n, d={}):
  if(n < 2):
    return 1
  else:
    return int(findFib(n-1) + findFib(n-2))

print(findFib(10))