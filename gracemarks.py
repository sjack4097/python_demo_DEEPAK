mark1=int(input("Enter first subject marks"))
mark2=int(input("Enter second subject marks"))
mark3=int(input("Enter third subject marks"))
if mark1>=40 and mark2>=40 and mark3>=40:
          per=(mark1+mark2+mark3)/3
          print("pass with percentage",per)
else:
     if mark1>=40 and mark2>=40 and mark3<40:
          if(mark3>32):
               print("pass")
     elif mark1>=40 and mark2<40 and mark3>=40:
          if(mark2>32):
               print("pass")
     elif mark1<40 and mark2>=40 and mark3>=40:
           if(mark1>32):
                print("pass")
     else:
          print("fail")
