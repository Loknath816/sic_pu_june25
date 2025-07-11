import binary_search 

def main():
    target = int(input(f"Enter the element to be searched:"))
    array_size = int(input("Enter the size of array: "))
    array = []
    print(f"Enter the array elements:")
    for i in range(array_size):
        array_element = int(input())
        array.append(array_element)
    array.sort()
    target_index =  binary_search.binary_search(target, array)
    if  target_index != -1 :
        print(f"{target} found at {target_index}th index of  the array,")
    else:
        print(f" Element {target} not found in the array")

if __name__ == "__main__":
    main()


