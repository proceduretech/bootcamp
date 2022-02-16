# find index of number
import math

array1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 131]
num = 99
lengthArray1 = len(array1)

while lengthArray1 >0:
    lengthArray1 = len(array1)
    middleArray1 = lengthArray1/2
    midRoundOff1 = math.floor(middleArray1)
    print(midRoundOff1)

    print(array1[midRoundOff1])

    if array1[midRoundOff1] == num:
        print("The Number " + str(num) + " was found at index " + str(midRoundOff1))
        break

    if num < array1[midRoundOff1]:  # 22>55
        array1 = array1[0: midRoundOff1]
        print(array1)

    else:
        array1 = array1[midRoundOff1: lengthArray1]
        print(array1)











