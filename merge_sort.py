'''
Сортировка слиянием

'''


def merge(left, right, comparator):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if comparator(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr, comparator=(lambda x, y: x < y)):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle], comparator)
    right = merge_sort(arr[middle:], comparator)
    return merge(left, right, comparator)
