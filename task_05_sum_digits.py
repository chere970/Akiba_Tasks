number=float(input("Enter your number: "))
sum=0

temp=number
while temp>0:
   reminder=temp%10
   temp=temp//10
   sum+=reminder
    
print(f"The of the digits = {sum}")