num = int(input("Enter the number to find : "))
num_list = [4,5,6,7,8,9,66,75,87,89]

left_index, middle_index = 0, 0
right_index = len(num_list)-1


while left_index < right_index:

    middle_index = (left_index + right_index)//2
    middle_number = num_list[middle_index]

    if num == middle_number:
        break
    elif num > middle_number:
        left_index  = middle_index + 1
    else:
        right_index = middle_index - 1

print(f"Index of number {num} is {middle_index}")
        

 