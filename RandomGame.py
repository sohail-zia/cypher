import random
number = random.randint(0,9)
print(number)
while True:
   user_no = int(input("Enter your number: "))

   if user_no == number:
    print("You won")
    break
   else:
    print("try again")
    continue