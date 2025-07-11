def get_data():
    
    array_size = int(input("Enter the size of array: "))
    array = []
    print(f"Enter the array elements:")
    for i in range(array_size):
        array_element = int(input())
        array.append(array_element)
    low = 0
    high = array_size - 1
   
    return   array, low, high

def quick_sort(array, low, high):
    if low < high : # means atleast 2 ele in array
        pivot_index = partition(array, low, high)
        quick_sort(array, pivot_index + 1, high)
        quick_sort(array, pivot_index, high)

       


def  partition(array, low , high):
   
    pivot = array[high]
    k = low 
    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[k] = array[k], array[i]
            k += 1
    array[k], array[high] = array[high], array[k]
    return k


array, low, high = get_data()

print(quick_sort(array, low, high))

