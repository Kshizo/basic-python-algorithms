StackArray=[]

def POP():
    if len(StackArray)<1:
        print("there are no elements to pop")
    else:    
        removed=StackArray.pop()
        print("the removed item is: ",removed)
        

def Push():
    x=int(input("input number to be pushed"))
    StackArray.append(x)


def options():
    while True:
        userInput=input("please input which action is to be taken: pop,push,display,exit")
        userInput=userInput.lower()

        if userInput=="push":
            Push()

        elif userInput=="pop":
            POP()

        elif userInput=="display":
            print(StackArray)
    
        else:
            userInput=="exit"
            break


options()
 
    
