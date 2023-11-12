
from cmath import sqrt
import math


class Search():

    def __init__(self) -> None:
        pass

    
    def linear(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1

    def binary_recursive(self, nums, target, left=None, right=None):
    
        if left == None and right == None:
            left = 0
            right = len(nums) - 1

        if right < left:
            return -1 

        middle_index = int((left + right) / 2)
        middle = nums[middle_index]

        if middle == target:
            return middle_index

        if target < middle:
            return self.binary_recursive(nums, target, left, middle_index - 1)
        else:
            return self.binary_recursive(nums, target, middle_index + 1, right)



    def binary_iteration(self, nums, target):

        middle_index = int(len(nums) / 2)
        middle = nums[middle_index]

        while middle_index != 0 and middle_index != len(nums)-1:

            if middle == target:
                return middle_index

            if target < middle:
                middle_index = int(middle_index / 2)
                middle = nums[middle_index]

            else:
                middle_index = int((middle_index + len(nums)) / 2)
                middle = nums[middle_index]

        return -1 

    def ternary(self, nums, target, left=None, right=None):
    
        if left == None and right == None:
            left = 0
            right = len(nums) - 1

        if right < left:
            return -1

        partition_size = int((left + right) / 3)
        mid_1 = left + partition_size
        mid_2 = right - partition_size

        if nums[mid_1] == target or nums[mid_2] == target:
            return mid_1 if nums[mid_1] == target else mid_2

        if target < mid_1:
            return self.ternary(nums, target, left, mid_1 - 1)
        elif target > mid_2:
            return self.ternary(nums, target, mid_2 + 1, right)
        else:
            return self.ternary(nums, target, mid_1 + 1, mid_2 -1)

    
    def jump(self, nums, target):
        block_size = int(math.sqrt(len(nums)))

        start = 0
        next = block_size


        while start < len(nums) - 1:
            if nums[next - 1] >= target:
                #if num is in array, it is in this section
                while start < next:
                    if nums[start] == target:
                        return start
                    start += 1

            else:
                #jump to next section
                start = next
                next += block_size

                if next > len(nums):
                    next = len(nums) -1

        return -1

    def exponential(self, nums, target):

        bounds = 1

        while bounds < len(nums) and nums[bounds] < target:
            bounds *= 2

        return self.binary_recursive(nums, target, bounds/2, min(bounds, len(nums) - 1))






def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search = Search()
    print(search.jump(numbers, 1))


if __name__ == "__main__":
    main()