def quicksort(arr):
    if(len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        leftSubArray = [element for element in arr[1:] if element <= pivot]
        rightSubArray = [element for element in arr[1:] if element > pivot]
        return quicksort(leftSubArray) + [pivot] + quicksort(rightSubArray)

def main():
    str_arr = input().split(' ') #will take in a string of numbers separated by a space
    arr = [int(num) for num in str_arr]
    print("input",arr)
    sorted_result = quicksort(arr)
    print('sorted_result',sorted_result)

main()