def binary_search(arr, x):
    iter = 0
    low = 0
    high = len(arr) - 1
    upper_lim = None

    while low <= high:

        mid = (high + low) // 2
        mid_value = arr[mid]
        iter += 1

        if mid_value < x:
            low = mid + 1

        elif mid_value > x:
            upper_lim = mid_value
            high = mid - 1

        else:
            upper_lim = mid_value
            break

    return iter, upper_lim

arr = [1.6, 2.4, 3.9, 4.3, 5.78, 6.34, 7.256, 8.12, 9.52, 10.5, 40.1]
x = 3
iter, upper_lim = binary_search(arr, x)
if upper_lim is not None:
    print(f"Елемент {x} знайдено за {iter} ітерацій. Верхня межа: {upper_lim}")
else:
    print(f"Елемент {x} не знайдено у масиві.")

