# Add 'ing' to the word if its length is greater than 3. Else print as it is.
# Add 'ly' if the given word has 'ing' in the end.


a=input('enter a string ', )
if (len(a)<3):
    print('string: ', a)
else:
    if (a.endswith('ing', 0,len(a))):
        a=a.replace('ing','ly')
        print('New string: ', a)
    else:
        b='ing'
        print(' New string: ', a+b)