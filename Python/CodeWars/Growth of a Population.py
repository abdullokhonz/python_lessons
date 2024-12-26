# def nb_year(p0, percent, aug, p):
#     year = 0
#     fifty_year = 0
#     while p0 <= p:
#         year += 1
#         fifty_year += 1
#         p0 += (p0 / 100) * percent
#         if fifty_year == 50:
#             p0 += aug
#             fifty_year = 0
#     return year

def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        count += 1
        p0 += p0 * (percent / 100) + aug
    return count


print(nb_year(1000, 2, 50, 1200))
