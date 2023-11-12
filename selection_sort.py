
class SelectionSort():

    def __init__(self) -> None:
        pass

    def sort(self, array : list):

        for i in range(len(array)):
            min_num = min(array[i:])
            min_index = array[i:].index(min_num) + i

            array[min_index] = array[i]
            array[i] = min_num

        return array
            
    

def main():
    sorter = SelectionSort()
    print(sorter.sort([]))


if __name__ == "__main__":
    main()