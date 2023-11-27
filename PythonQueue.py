names = []

for i in range (10):

    tempName = input("Enter a name: ")
    names.append(tempName)

print(names)

for i in range(len(names)):
    print(names[0])
    names.pop(0)
    
print(names)


