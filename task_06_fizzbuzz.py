starting_number=float(input("Enter your starting number: "))
ending_number=float(input("Enter your ending number: "))
for number in range(int(starting_number), int(ending_number)+1):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)