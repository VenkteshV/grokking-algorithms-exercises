def findSmallest(arr):
    smallest_element =arr[0]
    smallest_index =0
    for i in range(1, len(arr)):
       if(arr[i] < smallest_element):
           smallest_element = arr[i]
           smallest_index =i 
    return smallest_index

def selection_sort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr


def main():
    str_arr = input().split(' ') #will take in a string of numbers separated by a space
    arr = [int(num) for num in str_arr]
    print(arr)
    sorted_result = selection_sort(arr)
    print(sorted_result)

main()