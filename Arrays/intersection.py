a=[1,2,4,5,6]
b=[3,7,4,6,2]
count = {}
r = []

for i in a:
    count[i] = count.get(i,0)+1

for i in b:
    if i in count:
        r.append(i)

print(r)
