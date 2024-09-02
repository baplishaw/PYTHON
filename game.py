import random
computer=random.choice([-1,0,1])


yourstr=input("enter your choice")   #ENTER P=PAPPER,S=SCISSORS,R=ROCK  : IT SHOULD BE CAPITAL LETTERS 
youdict={ "S":1,"P":-1,"R":0}
revdict={  1:"scissors",-1:"paper",0:"rock"}
you=youdict[yourstr]  #1,-1,0 WILL BE STORED 


print (f" you choose {revdict[you]} \n computer choose  {revdict[computer]}")

if(computer==you):
    print("its a draw")
else:
    if(computer==-1 and you ==1):
        print("you win")    
    elif(computer==1 and you ==-1):
        print("you loose")
    elif(computer==0 and you==1):
        print("you loose")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==-1 and you==0):
        print("you loose")  
    else:
        print("somthing went wrong")      
                      

        
