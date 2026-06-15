# Find largest element in an array

arr = [10, 25, 8, 45, 12]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element =", largest)
