# '''
# input :array with n integers
# divide array into 2 parts with size x and size z such that x + y =n
# x[i]> p
# y[i]< p
#  x>1 and x< = 1000000
# how many p values you can take fulfilling above condition
# n = 6, x = 4, y = 2
# input_array = [1, 2, 7, 8, 23 , 24]
# p is in between 2 and 7

# x[i]> y[i]
# '''



# n, x, y = map(int, input().split())

# input_array = list(map(int, input().split()))


# input_array.sort()
# print(input_array)
# p =  input_array[y] - input_array[y - 1] - 1
# print(p)
    

def list_partitioners():
    n, x, y = map(int, input("Enter the size of input array, one part of array and other part:").split())
    input_array = []
    print(f"Enter the {n} array elements")
    for i in range(n):
        element = int(input())
        input_array.insert(i ,element )
    
    input_array.sort()
    print(f"the sorted  input array is : {input_array}")

    p = (input_array[y] - input_array[y - 1]) - 1
    print(f"the possible values of p that satisfies given condition:{ p}")

list_partitioners()




    



  