Desc=input("Please give a description of the image")
Wid=int(input("input width of image"))
Heigh=int(input("input height of the image"))
Framecol=input("input color of the frame")

class Picture:
    def __init__(self,Description,Width,Height,Framecolour):
        Desc=self.Description
        Wid=self.Width
        Heigh=self.Height
        Framecol=self.Framecolour


def Constructor(self):
    def GetDescription(self):
        print("the description you gave: ",Desc)

    def GetHeight(self):
        print("the width of the image: ",Wid)
        
    def GetWidth(self):
        print("the height of the image: ",Heigh)
        
    def GetColor(self):
        print("the color of the frame: ",Framecol)

             
Constructor()

userInput=input("please input what information you need,Description,Width,Height,Color")
userInput=userInput.lower()

if userInput=="height":
    GetHeight()

elif userInput=="description":                
    GetDescription()

elif userInput=="width":
    GetWidth()

elif userInput=="color":
    GetColor()
    
    
    








