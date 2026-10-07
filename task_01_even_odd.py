number=float(input("Enter a number: "))
if number%1==0:
  if number % 2 == 0:
    print(f"The number {number} is  even.")
  else:
    print(f"The number {number} is odd.")
else:
  print(f"The number {number} is not an integer.")