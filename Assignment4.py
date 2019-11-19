number=int(input("enter number of element"))
count=[]
odd=0
even=0
for i in range(number):
    p=int(input("enter numbers"))
    if(p%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)

