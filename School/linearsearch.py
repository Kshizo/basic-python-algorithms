#input number of elements in array
#input number to search
#search number and display whether number is found with location


u = int(input("Input the number of elements you want in the array: "))

arrayData = []

for g in range(u):
    x = int(input(f"Input element {g + 1} to put in array: "))
    arrayData.append(x)

def linearSearch(userInput):
    for i in range(len(arrayData)):
        if arrayData[i] == userInput:
            return True
    return False

userInput = int(input("Enter a value to search: "))
returnValue = linearSearch(userInput)
if returnValue:
    print("Value has been found")
else:
    print("Value is not found")







