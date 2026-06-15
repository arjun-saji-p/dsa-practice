# Find smallest element

arr = [10, 20, 5, 40, 30]

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)
