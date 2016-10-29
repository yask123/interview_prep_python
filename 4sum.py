arr = [1,2,4,5,6,13]

def get_comb_of_4(arr, target):

    comb_hash_map = {}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]
            if current_sum in comb_hash_map:
                comb_hash_map[current_sum].append((i,j))
            else:
                comb_hash_map[current_sum] = [(i,j)]

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]

            if target-current_sum in comb_hash_map:
                for x, y in comb_hash_map[target-current_sum]:
                    if i != x and i !=y and j!= x and j!=y :
                        print (arr[i], arr[j], arr[x], arr[y])
get_comb_of_4(arr,12)
