n = 10
m=10

max_val = float("-inf")
min_val = float("inf")
sum=0
even_count=0
odd_count=0

while n > 0:
    number = int(input("Enter a number: "))
    n -= 1
    sum+=number
    
    if number%2==0:
        even_count+=1
    else:
        odd_count+=1
    

    if number > max_val:
        max_val = number
    if number < min_val:
        min_val = number
average=float(sum/m)
    

print("Maximum number is:", max_val)
print("Minimum number is:", min_val)
print(f"Total sum of the numbers is {sum}.")
print(f"Average: {average}.")
print(f"Even number count: {even_count}")
print(f"Odd numbers count: {odd_count}")