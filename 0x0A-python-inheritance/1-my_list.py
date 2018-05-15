#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        """Use bubble sort to create a sorted list to print
        Args:
            self (list): unsorted list
        """
        arr = self[:]
        done = False
        while not done:
            done = True
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    done = False
        print(arr)

if __name__ == '__main__':
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
