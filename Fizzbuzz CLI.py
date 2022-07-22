for Zahl in range(1,60,1):
    if Zahl%5 == 0 and Zahl%3 == 0:
        print("Fizzbuzz")
    elif  Zahl%5 == 0:
        print("Buzz")
    elif  Zahl%3 == 0:
        print("Fizz")
    else:
        print(Zahl)


    
