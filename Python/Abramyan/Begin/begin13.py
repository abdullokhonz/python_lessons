print ("Begin13◦. Даны два круга с общим центром и радиусами R1 и R2 (R1 > R2). Найти площади этих кругов S1 и S2, а также площадь S3 кольца, внешний радиус которого равен R1, а внутренний радиус равен R2: S1 = π·(R1) ** 2, S2 = π·(R2) ** 2, S3 = S1 - S2")

import math

r1 = float(input("Введите радиус R1: "))
r2 = float(input("Введите радиус R2: "))
s1 = math.pi * r1 ** 2
s2 = math.pi * r2 ** 2
s3 = s1 - s2
print("Площадь первого круга (S1) = ", s1)
print("Площадь второго круга (S2) = ", s2)
print("Площадь кольца (S3) = ", s3)