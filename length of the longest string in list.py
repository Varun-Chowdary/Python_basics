# Enter a list and return the length of the longest string

i=eval(input('enter a list'))
g=[]
for j in i:
    g.append(len(j))
g.sort()
d=len(i)
print(g[d-1])