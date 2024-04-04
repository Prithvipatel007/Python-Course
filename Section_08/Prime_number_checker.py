def prime_checker(num):
    for i in range(2, num):
        isPrime = True
        if(num % i == 0):   # if the number is divided cleanly which means remainder is 0
            #Not a prime number
            isPrime = False

    if(isPrime == True):
        print("Its a prime number")
    else:
        print("Its not a prime number")

number = int(input("Enter your number : "))
prime_checker(num = number)