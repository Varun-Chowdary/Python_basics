# Check the no of characters that are in a user given sentence
#also print a histogram of frequencies



state=input('Enter a sentence')
state=state.lower()
Dict={}
for word in state:
    if word not in Dict:
        Dict[word]=1
    else:
        Dict[word]+=1
print(Dict)
for key,val in Dict.items():
    print(key, '\t', '*'*val)