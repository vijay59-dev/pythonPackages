arr = [1, 2, 3 ,18 ,7, 98, 181]
element_found_at_index = None


def linear_search(my_number):
    global element_found_at_index
    for i in range(len(arr)):
        if my_number == arr[i]:
            element_found_at_index = i
        else:
            pass

# printing the array to suggest user to choose the element to be searched
print(arr)
print('\n')
number_to_searched = int(input('enter the number from above array to be searched \n'))

#call the function
linear_search(number_to_searched)

# check if the element found or not
if element_found_at_index:
    print('element found at index: ',element_found_at_index)
else:
    print('entered number is not in the given array')