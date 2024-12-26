# try:
#     print(1 / 0)
# except Exception:
#     print(2)
# else:
#     print(3)
# finally:
#     print(4)
import io

# try:
#     print(int(input('>>>')))
# except ValueError:
#     print('ERROR!!!')

# try:
#     file = open('text.txt', 'r')
#     file.write('123')
# except (io.UnsupportedOperation, FileNotFoundError):
#     print('Файл не найден!')
# else:
#     print('Nice!')
# finally:
#     file.close()

# try:
#     print([i for i in range(3)][int(input('>>>'))])
# except IndexError:
#     print('Индекс выходит за пределы списка!')

# try:
#     file = open(input())
#     file.write('qwerty')
# except FileNotFoundError:
#     print('Файл не найден!')
# except PermissionError:
#     print('У вас нет разрешений на использование файла!')

# a, b, c = int(input()), int(input()), int(input())
# if a + a == b and a + a + a == c:
#     print('YES')
# else:
#     print('NO')
# print('YES' if a + a == b and a + a + a == c else 'NO')
