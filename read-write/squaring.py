def square(squareRange):
  for i in range(squareRange,0,-1):
    print(i*i)

def interactive():
  num = int(input("What's the largest number you'd like to square?"))
  square(num)

interactive()