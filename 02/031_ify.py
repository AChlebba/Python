aa = [None, {}, {'q': 12}]
bb = [None, "", "Ala"]

str_format2 = '{:^15} {:^15} {:^20} {:^25} {:^35} {:^20}'
print str_format2.format("a", "b",
            "a if a>b else b",
            "(a > b and [a] or [b])[0]",
            "(a > b and {0: a} or {0: b})[0]",
            "a > b and a or b")
for a in aa:
    for b in bb:
        print str_format2.format(a, b
                                , a if a > b else b
                                , (a > b and [a] or [b])[0]
                                , (a > b and {0: a} or {0: b})[0]
                                , a > b and a or b)

cd = [1]
dc = [1]
print dc[0]
print cd[0] is dc[0]
print [1] is [1]
