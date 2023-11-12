nums = [5, 4, 3, 2, 1]

swapped = False
i = 0
while i < len(nums):

    if i == len(nums) - 1:
        if swapped:
            i = -1
            swapped = False

        i += 1    
        continue

    if nums[i] > nums[i + 1]:
        temp = nums[i]
        nums[i] = nums[i + 1]
        nums[i + 1] = temp
        swapped = True

    i += 1

print(nums)


