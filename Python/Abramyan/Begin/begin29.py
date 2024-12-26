alpha = float(input("Введите значение угла α в градусах (0 < α < 360): "))

while alpha <= 0 or alpha >= 360:
    print("Введено некорректное значение угла α")
    alpha = float(input("Введите значение угла α в градусах (0 < α < 360): "))

radians = alpha * 3.14 / 180
print("Значение угла α в радианах:", radians)