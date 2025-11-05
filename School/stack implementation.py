#implementing stack

userList=[]

ListLength=int(input("enter list length"))
for i in range (0,ListLength):
    item=int(input("input value"))
    userList.append(item)

def PoP():
    bflag=False
    userList.pop()

def push():
    Value=int(input("please enter value to be pushed into stack"))
    userList.append(Value)
    bflag=False

def display():
    print(userList)

bflag=False
while bflag==False:
    Choice=str(input("choose whether you want to push,pop or display stack"))
    LChoice=Choice.lower()

    if LChoice=="pop":
        PoP()

    elif LChoice=="push":
        push()

    elif LChoice=="display":
        bflag=True
        display()
