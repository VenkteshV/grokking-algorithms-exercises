def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

def main():
    str_arr = input().split(' ') #will take in a string of numbers separated by a space
    arr = [int(num) for num in str_arr]
    print("input",arr)
    sorted_result = insertion_sort(arr)
    print('sorted_result',sorted_result)

main()