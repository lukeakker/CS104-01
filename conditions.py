# CS104
# Lucas Vandenakker
# conditions.py

repeat = True
while repeat:
    print("Enter the temperature")
    temp = input()
    
    if temp == "end" or temp == "End":
        repeat = False

    else:
        temp = int(temp)
        if temp > 90:
            print("Wear Shorts")
        elif temp > 70:
            print("Short sleeves are fine")
        elif temp > 50:
            print("Wear a jacket")
        elif temp > 32:
            print("Wear a heavy coat")
        else:
            print("Stay inside")



        
    
