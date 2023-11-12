from tkinter import N
from linked_lists import LinkedList
from counting_sort import CountingSort
class BucketSort():

    def __init__(self) -> None:
        pass

    
    def sort(self, nums : list, num_buckets):

        buckets = [LinkedList() for i in range(num_buckets)]

        for num in nums:
            index = int(num / num_buckets)
            print(index)
            buckets[index].addLast(num)


        count_sorter = CountingSort()
        i = 0
        for bucket in buckets:
            sorted = count_sorter.sort(bucket.toArray())
            for n in sorted:
                nums[i] = n
                i += 1


        return nums





def main():

    sorter = BucketSort()
    print(sorter.sort([5, 4, 3, 8, 2, 1, 1], 3))


if __name__ == "__main__":
    main()