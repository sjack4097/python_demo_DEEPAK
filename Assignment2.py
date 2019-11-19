n=int(input("Enter Number Of Elements :"))
l=[]
primeNumber = []
odd,even=0,0
for i in range(n):
    l.append(int(input("Enter Number :")))
for i in l :
    if(i%2==0):
        even+=1
    else:
        odd+=1
    if i > 1:
        for j in range(2,i):
            if(i % j) == 0:
                break
        else:
            primeNumber.append(i)
print("Number Of Even Numbers :",even)
print("Number Of Odd Numbers :",odd)
print("Prime Numbers In List :",primeNumber)
print("Largest Number :",max(l))
print("Smallest Number :",min(l))
