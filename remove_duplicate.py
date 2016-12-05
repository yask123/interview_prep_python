def remove_dups(arr):
    write_index = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            write_index += 1

        arr[write_index] = arr[i]

    return arr


a = [1, 1, 1, 1, 2, 2, 2, 2, 3]

remove_dups(a)
print a
