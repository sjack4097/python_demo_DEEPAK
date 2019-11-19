'''l1=[1,2,3,4,5,6]
for i in l1:
    if(i%2==0):
        print(i,"Is Even Number")
    else:
        print(i ,"Is Odd Number")
        
n=int(input("Enter value of n:"))
for i in range(0,n):
   l1=int(input("Enter Numbers:"))
print("Even Numbers:")
for i in l1:
    if(i%2==0):
        print(i)
'''

'''
n=int(input("Enter value of n:"))
for i in range(0,n):
    n1=int(input("Enter Number:"))
for i in range(0,n):
    if(i%2)==0:
        print(i,"Is Even Number")
    else:
        print(i ,"Is Odd Number")'''



#Even Odd Numbers
num=int(input("Enter Number:"))
if(num%2)==0:
        print(num,"is Even Number ")
else:
        print(num,"is Odd Number")
        

'''
#Prime Number:
num=int(input("Enter Number:"))
if num > 1:
    for i in range(2,num):
        if(num % i)==0:
            print(num,"is Not Prime Number")
            break
    else:
        print(num,"is Prime Number")
else:
    print(num," is Not Prime Number")
'''
