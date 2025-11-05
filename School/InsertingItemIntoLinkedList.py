#inserting item into linked list

''' nullPointer-1
 def LinkedListAdd(itemAdd):
     if heapStartPointer=nullPointer:
         print("linked list is full")

     else:'''

#from book

def insert(itemAdd):
    global startPointer
    if heapStartPointer==nullPointers:
        print("linked list is full")

    else:
        tempPointer=startPointer
        startPointer=heapStartPointer
        heapStartPointer=myLinkedListPointers[heapStartPointer]
        myLinkedList[startPointer]=itemAdd
        myLinkedListPointers[startPointer]=tempPointer
        
