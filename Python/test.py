n = int(input())
count = 0

for _ in range(n):
    message = input().strip()
    print(message)

    i = 0
    occurrences = 0
    while i < len(message):
        i = message.find("11", i)
        print(i)
        if i == -1:
            break
        occurrences += 1
        i += 2

    if occurrences >= 3:
        count += 1

print(count)
