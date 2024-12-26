def past(h, m, s):
    hm = 0
    mm = 0
    sm = 0
    if 0 <= h <= 23:
        for i in range(h + 1):
            hm += i * 3600000
    if 0 <= m <= 59:
        for j in range(m + 1):
            mm += j * 60000
    if 0 <= s <= 59:
        for k in range(s + 1):
            sm += k * 1000
    return hm + mm + sm


for h in range(0, 24):
    for m in range(0, 60):
        for s in range(0, 60):
            print(f'Hours: {h}; Minutes: {m}; Seconds: {s};', past(h, m, s))
