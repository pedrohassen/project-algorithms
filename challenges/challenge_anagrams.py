def merge_sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])
    return merge(left, right, list(string))


def merge(left, right, reunion):
    index_left = 0
    index_right = 0

    while index_left < len(left) and index_right < len(right):
        if left[index_left] <= right[index_right]:
            reunion[index_left + index_right] = left[index_left]
            index_left += 1
        else:
            reunion[index_left + index_right] = right[index_right]
            index_right += 1

    for index_left in range(index_left, len(left)):
        reunion[index_left + index_right] = left[index_left]

    for index_right in range(index_right, len(right)):
        reunion[index_left + index_right] = right[index_right]

    return ''.join(reunion)


def is_anagram(first_string, second_string):
    sorted_first_string = merge_sort(first_string.lower())
    sorted_second_string = merge_sort(second_string.lower())

    if (
        len(first_string) > 0
        and len(second_string) > 0
        and sorted_first_string == sorted_second_string
    ):
        return (
            sorted_first_string, sorted_second_string, True
        )
    return (
        sorted_first_string, sorted_second_string, False
    )
