def get_data():
    search_key = int(input(f"Enter the element to be searched:"))
    array_size = int(input("Enter the size of array: "))
    input_array = []
    print(f"Enter the array elements:")
    for i in range(array_size):
        array_element = int(input())
        input_array.append(array_element)
    return search_key and array_size and input_array
    


def binary_search(search_key, array_size, input_array):


    low = 0
    high = array_size - 1 
    mid = (low + high)//2

    while low <= high:
        if search_key == input_array[mid]:
            print(f"{search_key} found in index [mid]")
        
        elif search_key < input_array[mid]:
            high = mid - 1
        
        else:
            low = mid + 1
        
search_key, array_size, input_array = get_data()
# binary_search(search_key,array_size,input_array)
binary_search(search_key, array_size, input_array)



