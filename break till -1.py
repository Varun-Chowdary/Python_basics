n=int(input('enter a numb'))
count1=0
sum=0
count2=0
avg_even=0
avg_odd=0
while(n!=-1):
    k=0
    sum=sum+n   
    if(n%2==0):
        count1+=1
        avg_even+=n
        avg_even=avg_even/count1
    else:
        count2+=1
        avg_odd+=n
        avg_odd=avg_odd/count2
    n=int(input('enter a numb'))
print('total sum', sum)
print('avg even', avg_even)
print('avg_odd', avg_odd)
print('total count', count1+count2)
    
        4