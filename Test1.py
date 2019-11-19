key=["if","else","return","break"]
methods=["print","input","user"]
print("Enter String:")
i=input().splitlines()
print(i)
counts=dict()
for word in key:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
#return counts
print(counts)
