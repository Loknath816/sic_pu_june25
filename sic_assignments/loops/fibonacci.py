input_number = int(input("Enter the input number for nth fibonacci number  "))
First_term = 1
Second_term = 2
for i in range(3, input_number + 1):
    nth_term = First_term + Second_term
    
    First_term = Second_term
    Second_term = nth_term

# print(nth_term,"is the",input_number,"th fibonacci number")    
print(f"{nth_term} is the {input_number}th fibonacci number")


'''
1. understand the problem -> in fibonacci series every term is sum of previous two terms except first two terms of series
2. Identify input and output -> input is integer and output will be integer
3. model the computations -> i.e. after getting 3rd term, 2nd term will be 1st term and 3rd term will be second term for next number
\n 
'''