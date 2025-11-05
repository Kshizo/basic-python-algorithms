DataArray=[0,100]
def ReadFile()
    try:
        IntegerData="IntegerData.txt"
        File1=open (IntegerData ,'r')
        for i in range 1 to 100:
            DataArray[i]=File1.readline()
            DataArray=int(DataArray[i])
    except:
        print("file not found")
    
    
