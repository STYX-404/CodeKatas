def find_needle(haystack):
    x = "needle"
    if x in haystack:
        return ("found the needle at position "+ str(haystack.index(x)))