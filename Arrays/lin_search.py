# Linear Search

arr = [10, 20, 30, 40, 50]

key = 30

found = False

for num in arr:
    if num == key:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")
