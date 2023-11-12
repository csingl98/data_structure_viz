
class MergeSort():

    def __init__(self) -> None:
        pass

    def sort(self, nums : list):
        if len(nums) < 2:
            return

        middle = int(len(nums) / 2)

        left = nums[:middle]
        right = nums[middle:]

        self.sort(left)
        self.sort(right)

        self.merge(left, right, nums)

        return nums

    def merge(self, left, right, result):
        
        i = j = k =0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
                k += 1

            else:
                result[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            result[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            result[k] = right[j]
            k += 1
            j += 1

def main():
    sorter = MergeSort()
    print(sorter.sort([5, 4, 3, 8, 2, 1, 1, 10, 25, 25, 4]))


if __name__ == "__main__":
    main()