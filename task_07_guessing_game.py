import random

print("Gussing Game")
secret_number= random.randint(1, 100)
print("You will have 5 chances to guess the number between 1 and 100")
print(secret_number)

attempts=5

while attempts>0:
    number=float(input("Enter your number: "))
    if number==secret_number:
       print("Congrats!. You guessed it!")
       break
    else:
       
        attempts-=1
        if attempts>0:
           print(f"Not correct. {attempts} attempts left")
           
        else:
            print("Game Over!")
        #    number=float(input("Enter your number: "))
