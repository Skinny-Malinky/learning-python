def fizz_buzz(this_number):
  for i in range(this_number):
    if i%3 == 0 and i%5 == 0:
      print ('fizzbuzz')
    elif i%3 == 0:
      print('fizz')
    elif i%5 == 0:
      print('buzz')
    else: print(i)

fizz_buzz(20)