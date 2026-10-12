# password=int(input("Enter your 4-digit ATM PIN: "))
real_pin=1234
attempts=3
while attempts>0:
    password=int(input("Enter your 4-digit ATM PIN: "))
    attempts-=1
    if password==real_pin:
        print("Access Granted")
        break
    else:
        
        if attempts==0:
            print("Access Denied. Your account is blocked. Try after 1 hour.")
        else:
         print(f"\nIncorrect PIN. {attempts} attempts left. \n")
        