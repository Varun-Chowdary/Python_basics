n=int(input('enter a numb'))

for i in range (n):
    num=i
    l=len(str(num))
    result=0
    while(i!=0):
        
        k=i%10
        result=result+k**l
        i=i//10
    if (result==num):
        print('Armstrong numb', num)
        
        
        
        
        
#x=int(input("Enter Any Number: "))
#for i in range(x):
 #   num=i
  #  result=0
   ##
   #while(i!=0):
    #    digit=i%10
     #   result=result+digit**n
      #  i=i//10
    #if num==result:
     #   print(num