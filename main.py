import random 
n = random.randint(1,100) 
a = 1
guesess = 1
while (a!=n):
    a = int(input("guess  a number"))
    if (a>n):
        print("Lower number please")
        guesess += 1
    elif(a<n):
        print("Higher number please")
        guesess += 1
print(f"You have gussed the number correctly in {guesess} attempt and the number is {n}")
