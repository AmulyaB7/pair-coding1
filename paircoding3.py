def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)
        return

    arr.sort()

    small = arr[1]

    large = arr[n - 2]

    print("Second smallest is", small)
    print("Second largest is", large)


if __name__ == "__main__":
    
    arr = list(map(int, input().split()))
    
 
    n = len(arr)
    
getElements(arr, n)