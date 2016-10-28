def max_ones(arr,m):

    start_index = 0
    end_index = 0

    arr_length = len(arr)

    no_of_zeros = m
    max_start_index = 0
    max_end_index = 0
    current_length = 0
    max_length = 0

    while end_index <= arr_length-1 :

        if arr[end_index] == 0:
            no_of_zeros -=1

        if no_of_zeros < 0:
            #Reset the start_index
            current_length = (end_index - start_index)
            if current_length > max_length:
                max_start_index = start_index
                max_end_index = end_index-1
            for i in range(start_index+1, end_index):
                if arr[i] == 0:
                    start_index = i+1
                    break
            no_of_zeros = 0
        end_index += 1

    if current_length > max_length:
        max_start_index = start_index
        max_end_index = end_index-1

    return max_start_index, max_end_index
