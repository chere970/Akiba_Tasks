number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if number1 == number2 == number3:
    print("All three numbers are equal.")
elif number1 >= number2 and number1 >= number3:
    if number1 == number2:
        print(f"The largest number is {number1}. The first and second numbers are equal.")
    elif number1 == number3:
        print(f"The largest number is {number1}. The first and third numbers are equal.")
    else:
        print(f"The largest number is {number1}.")
elif number2 >= number1 and number2 >= number3:
    if number2 == number3:
        print(f"The largest number is {number2}. The second and third numbers are equal.")
    else:
        print(f"The largest number is {number2}.")
else:
    print(f"The largest number is {number3}.")