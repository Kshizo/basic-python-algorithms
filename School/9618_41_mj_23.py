#9618/41/mj/23

AnimalList=[]
ColorList=[]

global AnimalTopPointer
global ColourTopPointer

AnimalTopPointer=0
ColourTopPointer=0

def ushAnimal(DataToPush):
    if AnimalTopPointer==20:
        print("Animal List has no space")
    else:
        AnimalList.append(DataToPush)
        AnimalTopPointer=AnimalTopPointer+1
        print("item has been pushed")


def PopAnimal:
    if AnimalTopPointer=0:
        print("")
    else:
        ReturnData=AnimalList.pop(ReturnData)
        AnimalTopPointer=AnimalTopPointer-1
        print(ReturnData)

def ReadData:
    AnimalFile=open('AnimalData.txt','read')
    for f in range(0,19,1):
        AnimalList.append(AnimalFile.readline())

def PushColour(DataToPush):
    global ColourTopPointer

    if ColourTopPointer==10:
        print("Colour List has no space")
    else:
        ColourList.append(DataToPush)
        ColourTopPointer=ColourTopPointer+1
        print(ColourList)

def PopColour:
    if ColourTopPointer==0:
        print("not items to push")
    else:
        ReturnData=ColourList.pop(ReturnData)
        ColourTopPointer=ColourTopPointer-1
        print(ReturnData)
    
        
        
