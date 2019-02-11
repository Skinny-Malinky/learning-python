# def findFib(n, d={}):
#   if n not in d.keys():
#     if n < 2:
#       d[n] = 1
#       return d[n]
#     else:
#       d[n] = findFib(n-1) + findFib(n-2)
#   print(d)
#   return d[n]

# print(findFib(10))

# ------------------
# Recursive function showing that a is an instantiator
# and a is stored locally
# 
# def add(n, a=[]):
#   a.append(n)
#   print(a)

# for i in range(10):
#   add(i)
#   a = []
#   print(id(a))
# add(56)

# ------------------
# Same as def add w/ explicit a definition
#
# def f: 
#   if (!a) a = []
#   def add2(n, a):
#     # print(id(a))
#     a.append(n)
#     print(a)
#
# ------------------
# Proof that c points to a
#
a = []
b = a 
c = b  
c.append(1)
print b