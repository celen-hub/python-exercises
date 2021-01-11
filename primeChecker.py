def prime_checker(number):
  for x in range(2, (number)):
    primerino = True
    if number % x == 0:
      primerino = False
  if primerino:
    print("It's prime")
  else:
    print("Not prime")



n = int(input("Check this number: "))
prime_checker(number=n)
