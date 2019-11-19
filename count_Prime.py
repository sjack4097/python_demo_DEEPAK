prime_no=0
n=int(input("Enter value of n:"))
if n>1:
    for i in range(2,n):
        list1=int(input("Enter Number:"))
        if(list1%i)==0:
            prime_no+=1
            break
        else:
            print("Number is Prime")
else:
    print("Number is not prime")
print("Prime Numbers Present in List:",prime_no)


