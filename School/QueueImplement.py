Queue = []

QueueFull = int(input("Please define the length of the queue: "))

def enqueue():
    if len(Queue) < QueueFull:
        item = input("Enter item to enqueue: ")
        Queue.append(item)
        print("Item enqueued successfully.")
    else:
        print("Queue is full, cannot enqueue more items.")


def dequeue():
    if len(Queue) > 0:
        item = Queue.pop(0)
        print("Dequeued item:", item)
        
    else:
        print("Queue has no items.")



while True:
    UserChoice = input("Please choose whether you would like to enqueue(1), dequeue(2) or exit(3): ")
    
    if UserChoice == "1":
        enqueue()
        
    elif UserChoice == "2":
        dequeue()
        
    elif UserChoice == "3":
        print("Queue:")
        print(Queue)
        break
               
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
