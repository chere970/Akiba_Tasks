number=int(input("Enter Positive Number: "))
temp=number
count_even=0
count_odd=0
sum=0
while temp>0:
    reminder=temp%10
    temp=temp//10
    sum+=reminder
    if reminder%2==0:
        count_even+=1
    else:
        count_odd+=1
print(f"Count of Even digits = {count_even}")
print(f"Count of Odd digits = {count_odd}")
print(f"Sum of the digits = {sum}")
    
    

