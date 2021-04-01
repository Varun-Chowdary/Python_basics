# To get the maximun and minimum values in a dict


dict={'hello':23,'marks':98,'sun':68}
list1=list()
for i,j in dict.items():
    list1.append(j)
maxlist=max(list1)
minlist=min(list1)
print(maxlist)
print(minlist)