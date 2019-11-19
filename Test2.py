print("Food Items")
l1=["Dosa","samosa","Pav Bhaji","Kachori","Chicken Biryani","Sandwich"]
print(l1)
l1[0]="Vada Pav"
print(l1)
l1.insert(0,"Masala Dosa")
l1.insert(2,"Panir Roll")
l1.pop(-2)
print(l1)

print("-------------------------------------------------------")
l2=["sope","Tooth Brush","shampoo","Backet","Towel"]
print(l2[0:3])
l2.insert(0,"Water")
if 'shampoo' in l2:
    print("shampoo is Present in List")
else:
    n=input("Enter Specific Item Name")
    l1.append(n)
    print(l1)
    

print(l2)
l2.pop(2)
print(l2)
n=input("Enter Specific Item NAame")

print("-------------------------------------------------------")
print("List 1 and List2:")
l3=l1+l2
print(l3)
print(len(l3))

