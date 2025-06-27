number_of_lines = int(input("Enter the number of lines of Rhombus :"))



for i in range(1, number_of_lines + 1):
    print(" " * (number_of_lines - i), "$ " * i,  sep = "", end = '')
    print("$ " * (number_of_lines - i))

# for i in range(1, number_of_lines+1):
#     print(" " * (number_of_lines - i), "$ " * i, sep = '')

# for i in range(number_of_lines,0,-1):
#     print(" " * (number_of_lines - i), "$ " * i,  sep = "")