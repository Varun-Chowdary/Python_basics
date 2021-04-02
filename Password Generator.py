#Password Generator (Weak or strong)

import random
n=input('What type of password do you want? Weak or Strong ',) #User Input
list1=['grapedwine','downsyndrome', 'celestialbodies','goodwills','badnames','loyalbunnies'] 
#random names for weak password
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#All Chars
if n=='Weak'or n=='weak':
    print('Your password is :', random.choice(list1))
elif n== 'Strong' or n=='strong':
    print('Your password is :', "".join(random.sample(s,8)))
    
    