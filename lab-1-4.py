def printDivisors(num):
    divisors = list()
    for i in range(1, num+1, 1):
        if num % i == 0:
            divisors.append(i)
    print(divisors)


number = int(input("ENter a natural number"))

printDivisors(number)
