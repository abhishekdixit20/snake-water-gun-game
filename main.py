'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1,0,1])               # this will chosee randomly from given list 
yourstr=input("Enter your choice:")              # this takes input form user in string form
yourdict={"snake":1,"water":-1,"gun":0}          # It is dictionery for fetching values 
mydict={1:"Snake" ,-1:"Water",0:"Gun"}           # It is only created for showing result in nice way mainly for f string

you= yourdict[yourstr]                           # the variable (you) store value from dictionery after taking input
                                                 # from user

print(f"You choosed: {mydict[you]}\nComputer choosed: {mydict[computer]}") # this show results in a real look 

if(computer==you): # If help to compare value between computer and user 
    print("Its a draw!")

else:
    if(computer==-1 and you == 1):
        print("You Win!")

    elif(computer==1 and you ==0):
        print("You Win!")

    elif(computer==0 and you ==-1):
        print("You Win!")

    elif(computer==-1 and you ==0):
        print("You loose!")

    elif(computer==1 and you ==-1): 
        print("You loose!")

    elif(computer==0 and you ==1):
        print("You loose!")

    else:
        print("Hackerrrrr!")