'''
Created on Dec 2, 2017

@author: ITAUser
'''
'''
Created on Nov 4, 2017

@author: ITAUser
'''
f = open('constituton.txt', 'r')
text = f.read()
words = text.split() 
num_words = len(words)
print(str(num_words))
