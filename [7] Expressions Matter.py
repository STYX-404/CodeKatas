def expression_matter(a, b, c):
    p1 = a * (b + c)
    p2 = a + b * c
    p3 = a * b * c
    p4 = (a + b) * c
    p5 = a + b + c
    results = [p1,p2,p3,p4,p5]
    results.sort()
    return results.pop()