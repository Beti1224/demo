def exponentialSearch(arr, n, x):
    # If x is present at the first location itself
    if arr[0] == x:
        return 0

    # Find range where x is present using exponential search
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    # Call binary search for the found range.
    return binarySearch(arr, i // 2, min(i - 1, n - 1), x)
