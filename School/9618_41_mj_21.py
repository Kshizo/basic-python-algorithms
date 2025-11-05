


arrayData = [10,5,6,7,1,12,13,15,21,8]
for i in range(0,9):
    for q in range(0,9):
        if  arrayData[q]<arrayData[q+1]:
            temp=arrayData[q]
            arrayData[q]=arrayData[q+1]
            arrayData[q+1]=temp
                    

print(arrayData)


       













""" class treasureChest:
    def __init__(self,questionP,answerP,pointsP):
        self.__question=questionP
        self.__answer=answerP
        self.__points=points 

userInput= int(input("enter a value to search"))
returnValue = linearSearch(userInput)
if returnValue == True:
    print("Value has been found")
    
elif returnValue == False:
    print("value is not present") 

def linearSearch(userInput):
    for i in range(0,10):
        if arrayData[i] == userInput:
            return True
    return False"""
