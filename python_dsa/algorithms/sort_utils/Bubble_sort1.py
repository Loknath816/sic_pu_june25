def get_data():
    
    array_size = int(input("Enter the size of array: "))
    input_array = []
    print(f"Enter the array elements:")
    for i in range(array_size):
        array_element = int(input())
        input_array.append(array_element)
    return  array_size , input_array

def bubble_sort1(array_size, input_array):
    # Assume input size to be N
    for i in range(0,array_size-1):
        for j in range(0,(array_size - 1) - i ):
        
            if input_array[j] > input_array[j+1]:
                 input_array[j], input_array[j+1] =  input_array[j+1], input_array[j]
    
    print(f"sorted array is : {input_array}" )

# The outer loop Runs through the list (Accessing elements of the list exactly once)
# The inner loop compares consecutive elements of the unsorted list

array_size, input_array = get_data()
bubble_sort1(array_size, input_array)
