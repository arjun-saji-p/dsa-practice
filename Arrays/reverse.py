# Reverse an array

arr = [1, 2, 3, 4, 5]

arr.reverse()

print(arr)


nums = [1,2,3,4,5]

n = len(nums)

for i in range(n // 2):
    nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]

print(nums)
