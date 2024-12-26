def better_than_average(class_points, your_points):
    all_class_points = 0
    for i in class_points:
        all_class_points += i
    return all_class_points / len(class_points) < your_points


print(better_than_average([2, 3], 5))
