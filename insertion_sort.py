
class InsertionSort():

    def __init__(self) -> None:
        pass

    def sort(self, nums : list):

        for i in range(len(nums)):
            current = nums[i]

            j = i - 1

            while j >= 0 and nums[j] > current:
                nums[j + 1] = nums[j]
                j -= 1
            
            nums[j + 1] = current


        return nums
    

def main():
    sorter = InsertionSort()
    print(sorter.sort([5, 4, 3, 2, 1, 1, 1]))


if __name__ == "__main__":
    main()