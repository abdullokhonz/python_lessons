def number(bus_stops):
    result = 0
    for i in range(len(bus_stops)):
        result += bus_stops[i][0] - bus_stops[i][1]
    return result


# def number(bus_stops):
#     return sum([stop[0] - stop[1] for stop in bus_stops])


print(number([[10, 0], [3, 5], [5, 8]]))
