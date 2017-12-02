'''
Created on Dec 2, 2017

@author: ITAUser
'''
def countingLetters(filename, mychar):
    f = open(filename, "r")
    count = 0
    run = True
    while run:
        letter = f.read(1)
        letter = letter.lower()
        if letter == "":
            break
        else:
            if letter == mychar:
                count = count + 1
    print(count)
    
countingLetters("constituton.txt", "a")