from timeit import default_timer as timer

from utils.test_helper import *
from sorting.insertion import InsertionSort
from sorting.selection import SelectionSort

if __name__ == "__main__":
    test = createArray(10000)

    sorter = InsertionSort()
    start = timer()
    sorted = sorter.sort(test)
    end = timer()

    if checkArray(sorted):
        print("insertion: ", end - start)
    else:
        print("InsertionSort failed.")

    sorter = SelectionSort()
    start = timer()
    sorted = sorter.sort(test)
    end = timer()

    if checkArray(sorted):
        print("selection: ", end - start)
    else:
        print("SelectionSort failed.")

#    print (*sorted)