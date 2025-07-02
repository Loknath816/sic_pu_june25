'''
arrange boys and girls in increasing order such that, no two boys and two girls are adjacent to each other \
(if that condition not given,answer would be simple -> join two arrays and sort it)
b[] , g[] ->given(input)
'Yes' if we can solve problem, 'No' if we cant (output)
b = [160, 170, 171, 173]
g = [180, 155, 161, 154]

sort b[]
sort g[] -> [154, 155, 161, 180]

compare b[0] and g[0]
if g[0] < = b[0] then check if b[i] <= g[i+1]| else order[0] = b[0]

[g,b,g,b]

'''
def valid_arrangement():
    T = int(input("Enter number of times test case should be ran: "))
    for i in range(T):
        N = int(input("Enter the  number of boys and girls of class:"))
        girls_height = []
        print("Enter the height of girls :")
        for i in range(N):
            num = int(input())
            girls_height.append(num)
        print(f"{girls_height} is list of height of girls")
        boys_height = []
        print("Enter the height of boys: ")
        for i in range(N):
            num = int(input())
            boys_height.append(num)
        print(f"{boys_height} is list of height of boys")
        arrangement = False

        for i in range(1,N):
            if girls_height[0] <= boys_height[0]:
                if boys_height[i-1] <= girls_height[i]:
                    arrangement = True
            
            else:
                if girls_height[i-1] <= boys_height[i]:
                    arrangement = True

        if arrangement:
            return "YES"
        else:
            return "N0"

print(valid_arrangement())