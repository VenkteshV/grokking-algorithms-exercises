def merge(arr, leftArray, rightArray):
    i = j = k = 0
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            arr[k] = leftArray[i]
            i+=1
        else:
            arr[k] = rightArray[j]
            j+=1
        k+=1

    while i < len(leftArray):
            arr[k]  = leftArray[i]
            k+=1
            i+=1

    while j < len(rightArray):
            arr[k] = rightArray[j]
            k+=1
            j+=1

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftSubArray = arr[:mid]
        rightSubArray = arr[mid:]
        mergesort(leftSubArray)
        mergesort(rightSubArray)
        merge(arr, leftSubArray, rightSubArray)

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end = ' ')

def main():
    str_arr = input().split(' ') #will take in a string of numbers separated by a space
    arr = [int(num) for num in str_arr]
    print("input",arr)
    mergesort(arr)
    print('sorted_result',arr)

main()

