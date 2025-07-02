'''
right rotation of given word -> put string in circle and rotate
 circle right you get different right rotations of a word
solutions:
1. slicing 
2. looping
3

college
ecolleg
gecolle
egecoll
legecol
llegeco
ollegec

collegeecolleg

'''
def is_same_reflection(word_1, word_2)  :
    temp = word_1 + word_2
    temp.find(word_1)
    # if word_1 in temp:
    #     return 1
    # else:
    #     return -1 


print(is_same_reflection('college', 'ecolleg'))

