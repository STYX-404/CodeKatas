def tupling(char, count):
    lst_to_tuple = []
    lst_to_tuple.append(char)
    lst_to_tuple.append(count)
    result_tuple = tuple(lst_to_tuple)
    return result_tuple

def ordered_count(input):
    result_lst = []
    chars_lst = []
    word_length = len(input)
    for i in range(0, word_length):
        count_of_char = 1
        for j in range(i + 1, word_length):
            if input[j] == input[i]:
                count_of_char += 1
        if input[i] not in chars_lst:
            result_lst.append(tupling(input[i], count_of_char))
        chars_lst.append(input[i])

    return result_lst