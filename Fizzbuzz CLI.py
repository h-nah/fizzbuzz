for Zahl in range(1,60,1):
    if Zahl%3 == 0:
        print("Fizz")
    if Zahl%5 == 0:
        print("Buzz")
    if Zahl%5 == 0 and Zahl%3 == 0:
        print("Fizzbuzz")
    else:
        print(Zahl)
