import math
number_of_lines = int(input("Enter the number of lines of Hollow Square :"))


for i in range(1, number_of_lines+1):



    if i == 1 or i ==  number_of_lines :
        print("$ " * number_of_lines)
    
    elif (i == math.ceil(number_of_lines / 2) ):
    
        print("$ ", "  ", "0 ","  ", "$ ", sep = "")

    else:
        print("$ ", "\ ", "  ", "/ ","$ ",  sep = '')

# for i in range(1, number_of_lines+1):
#     print("$ " * number_of_lines)