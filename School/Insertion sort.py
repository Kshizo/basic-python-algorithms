#Implement an insertion sort

myList=[2,5,4,1,6,7,4,9,3]

upperBound=9
lowerBound=0

for index in range(lowerBound+1,upperBound):
    key=myList[index]
    place=index-1
    if myList[place]>key:
        while place >=lowerBound and myList[place]>key:
            temp=myList[place+1]
            myList[place+1]=myList[place]
            myList[place]=temp
            place=place-1
        myList[place+1]=key

print(myList)
        
