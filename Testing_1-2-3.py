def number(lines):
    line_num = 1
    res = []

    for i in lines:
        i = str(line_num) + ": " + i
        res.append(i)
        line_num += 1
    return res