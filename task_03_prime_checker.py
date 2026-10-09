num = int(input("Enter a whole number: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True

    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
        
        
        # we need to check the loop upto number/2, because a number cannot be divided by any number greater than its half (except itself).