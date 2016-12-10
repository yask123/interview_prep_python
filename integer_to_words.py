'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

convert(19,323,984) = convert(19) + " million " + convert(323) + " thousand " +
convert(984)

'''


def convert(number):
    small = ['one', 'two', 'three', 'nineteen']
    tens = ['', '', 'hundred', 'thousand', 'million', 'billion']

    result = ''

    chunk_count = 0

    while number > 0:
        if number % 1000 > 0:
            result += convert_chunk(number % 1000) + ' ' + tens[chunk_count]

        number = number / 1000
        chunk_count += 1


def convert_chunk(number, small):
    if number >= 100:
        hundred_part = small[number / 100]
        number = number % 100
