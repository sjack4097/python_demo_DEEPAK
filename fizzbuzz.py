number=int(input("enter value"))
for i in range(1,number+1):
    if(i%3==0 and i%5==0):
        print(i,"it is FizzBuzz")
    elif(i%3==0):
        print(i,"it is Fizz")
    elif(i%5==0):
        print(i,"it isBuzz")
    else:
        print(i,"is not divisible by 3 and 5")
