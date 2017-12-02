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
    return count 
import string 
c = countingLetters
#make a list with the alphabet 
letters = list(string.ascii_lowercase)

#make a list thats stores the value of every letter
letnum = []
#make a loop that counts how many of each number there are
for i in letters:
    counts = countingLetters("constituton.txt",i)
    letnum.append(counts)


#define max number of value list
maxval = max(letnum)
#find letter with max value 
index = letnum.index(maxval)
let = letters[index]
    
    
#print answer
print(let,maxval)