import math
import random as rand

def solution(area):
    print(area)
    # sets range of acceptable values
    if area >= 1 and area <= 1000000 and isinstance(area, int) == True:
        list = []

        # while loop that searches for numbers that are close to total area
        while (True):
            # resets variables that check for valid numbers
            x = 0
            z = 0
            if area <= 4:
                list.append(area)
                break

            # performs loop until area a number 'z' can no longer be raised to the 2nd to be greater
            while (area > 4):
                
                # if x^2 results in an integer larger than the current area,
                # it subtracts current 'z' value with the area to find the next limit
                if x**2 >= area:          
                    list.append(z)
                    area -= z
                    break
                
                # if x^2 falls within the range, the operation continues
                else: 
                    z = x**2
                    x += 1
                    
        print(list[(len(list)-1)])
        print(list[(len(list)-2)])

        # if the final item is not equal to 1 subtracts it so there are several smaller squares 
        if list[(len(list)-1)] != 1 and list[(len(list)-1)] != 4:
            #removes element from list and stores it in a
            a = list.pop(len(list)-1)

            #subtracts 1 for each thing
            while a != 0:
                a -= 1
                list.append(1)

        return list

    else:
        list = []
        return list

    
x = 0
while x <= 10:
    print(solution(rand.randint(-1000000, 1000000)))
    print("\n")
    x += 1
