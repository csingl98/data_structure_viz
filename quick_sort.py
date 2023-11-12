
class QuickSort():

    def __init__(self) -> None:
        pass

    
    def sort(self, nums : list, start=None, end=None):
        if start == None and end == None:
            start = 0
            end = len(nums) -1

        if start >= end:
            return

        boundary = self.partition(nums, start, end)
        #left
        self.sort(nums, start, boundary -1)
        #right
        self.sort(nums, boundary + 1, end)

        return nums

    def partition(self, nums, start, end):
        pivot = nums[end]
        boundary = start - 1

        i = start
        while i < len(nums):
            if nums[i] <= pivot:
                boundary +=1
                temp = nums[boundary]
                nums[boundary] = nums[i]
                nums[i] = temp

            i += 1

        return boundary

def main():
    sorter = QuickSort()
    print(sorter.sort([5, 4, 3, 8, 2, 1, 1]))


if __name__ == "__main__":
    main()