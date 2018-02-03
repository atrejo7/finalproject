'''
Created on Feb 3, 2018

@author: ITAUser
'''
prime = input("insert a number:")
prime = int(prime)
for i in range(2,prime):
    if prime%i == 0:
        print (str(prime) + " is not a prime number.")
        break
    else:
        print (str(prime) + " is a prime number.")
        break
        
        
        
    

