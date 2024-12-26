def sum_array(arr):
    if arr == [] or arr == None:
        return 0
    if len(arr) == 1:
        return arr[0]
    arr.remove(min(arr))
    arr.remove(max(arr))
    return sum(arr)


print(sum_array([1, 2, 3]))
