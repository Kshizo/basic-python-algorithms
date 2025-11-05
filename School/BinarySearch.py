#BinarySearch

myList=[2,3,5,7,8,9,10,12,13,17]

upperbound=9
lowerbound=0

item=int(input("please input item to be found"))

found=False
while found==False:
    index=int((upperbound+lowerbound)/2)
    if item==myList[index]:
        found=True

    if item>myList[index]:
        lowerbound=index+1

    if item<myList[index]:
        upperbound=index-1

if found==True:
    print("item found at index number:",index+1)

if found==False:
    print("item is not present in the list")
    
