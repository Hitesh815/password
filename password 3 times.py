name="mary"
counter=0
print('hello mary')
while counter<3:
    password=input("password:")
    counter+=1
    if password=="swordfish":
        print("correct password")
        break
    elif password!="swordfish" and counter<3:
        
        print("wrong password")
        print("try again")
print("you entered the wrong password too many times")
print("exiting")
exit() 
#initially main  exiting wala if statement laga kar kar raha tha but uski zaroorat nahi hai
#if counter==3: iski zaroorat nahi hai kyunki while to jaise hi 3 hogi to false ho jaayegi to it will skip to whatever is in the end.
#aur counter elif me nahi  pehle hi daalna tha aazmi ne bataya kyunki main elif me le raha tha but baaki kal.














