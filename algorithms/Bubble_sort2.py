def get_data():
    
    array_size = int(input("Enter the size of array: "))
    input_array = []
    print(f"Enter the array elements:")
    for i in range(array_size):
        array_element = int(input())
        input_array.append(array_element)
    return  array_size , input_array


def bubble_sort2(array_size, input_array ):
    for i in range(0, array_size - 1):
        sorted = True # Assume the list is already sorted
        for j in range(0, (array_size - 1) - i):
            if input_array[j] > input_array[j+1]:
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
                sorted = False
        if sorted:
            break 
    # return input_array # gave TypeError :'list' object is not callable
    print(f"The sorted array is {input_array}")
array_size, input_array = get_data()
bubble_sort2(array_size, input_array)