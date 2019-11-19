n=int(input("Enter the value of n :"))
L=[]
for i in range (n):
    L.append(int(input("Enter the value")))
    area=3.14*L[i]*L[i]
    print("Area is",area)
