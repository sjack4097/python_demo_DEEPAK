n=int(input("Enter the value  of n :  "))
p=int(input("Enter the value  of  median :  "))
i=0
L=[]
L1=[]
L2=[]
for i in range (n):
    L.append(int(input("Enter the value")))

for i in range(len(L)):
    if(L[i]>p):
        L1.append(L[i])
    else:
         L2.append(L[i])
print("values greater than median ")
print(L1)
print("values less than median ")
print(L2)


