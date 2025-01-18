nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
total = len(nums)

index = 0
for i in range(1, total):
    if nums[i] != nums[index]:
        index += 1
        nums[index] = nums[i]

k = index + 1

result = nums[:k] + ['_'] * (total - k)
print((k, result))
