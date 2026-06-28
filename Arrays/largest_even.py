largest = None

for num in nums:
    if num % 2 == 0:
        if largest is None or num > largest:
            largest = num

print(largest)
