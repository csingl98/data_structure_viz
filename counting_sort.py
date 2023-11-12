
class CountingSort():

    def __init__(self) -> None:
        pass

    
    def sort(self, nums : list):

        max_num = max(nums) + 1
        counts = [0] * max_num

        for num in nums:
            counts[num] += 1

        index = 0
        for i in range(max_num):
            while counts[i] > 0:
                nums[index] = i
                counts[i] -= 1
                index += 1

        return nums



def main():
    sorter = CountingSort()
    print(sorter.sort([5, 4, 3, 8, 2, 1, 1]))


if __name__ == "__main__":
    main()