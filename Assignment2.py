even_no,odd_no=0,0
n=int(input("Enter value of n:"))
for i in range(0,n):
    list1=int(input("Enter Number:"))
    if(list1%2)==0:
        even_no+=1
    else:
        odd_no+=1
print("Even Numbers Are:",even_no)
print("Odd Numbers Are:",odd_no)

