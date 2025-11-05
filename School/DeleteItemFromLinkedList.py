#dELETING AN iTEM IN LINKED LIST
def delete(itemDelete):
    global startPointer,heapStartPointer
    if startPointer==nullPointer:
        print("Linked List empty")

    else:
        index=startPointer
        while myLinkedList[index] != itemDelete and index != nullPointer:
            oldindex=index
            index=myLinkedListPointers[index]
            
            if index==nullPointer:
                print("Item",itemDelete,"not found")

            else:
                myLinkedList[index]=None
                tempPointer=myLinkedListPointers[index]
                myLinkedListPointers[index]=heapStartPointer
                heapStartPointer=index
                myLinkedListPointers[oldindex]=tempPointer
                
