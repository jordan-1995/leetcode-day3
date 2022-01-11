def longestSubstring(s):
    if len(s) == 0:
        return 0

    sub_string = ""
    max_length = 0

    for elem in s:
        if elem in sub_string:
            sub_string = sub_string[sub_string.index(elem)+1:] + elem
        else:
            sub_string += elem
            if len(sub_string) > max_length:
                max_length += 1

    print(max_length)

longestSubstring("akshay")