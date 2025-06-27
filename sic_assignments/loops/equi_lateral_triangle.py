number_of_lines = int(input("Enter the number of lines of right angled triangle:"))


for i in range(1,number_of_lines+1):
   print(" " * (number_of_lines - i), "$ " * i, sep = "")

'''
for i = 1,     *
for i = 2,    * *
for i = 3,   * * *
for i = 4,  * * * *
for i = 5, * * * * *
'''
# " " * ((number_of_lines + 1) - i) -> will print whitespaces
# "$ " * i -> will print $ symbol with one white space
# sep = "" joins both meaning no space will be printed after printing whitespace before $ symbol