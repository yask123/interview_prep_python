def my_sqrt(x):
    if x <= 1:
        return x

    start = 1
    end = x

    while start <= end :
        mid = (start+end)/2
        guess_sqr = mid*mid

        if guess_sqr == x:
            return mid
        elif guess_sqr < x:
            start = mid+1
        else:
            end = mid-1
    return start-1

print (my_sqrt(10))
