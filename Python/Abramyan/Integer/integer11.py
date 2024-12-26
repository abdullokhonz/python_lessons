s = 0
p = 1
for i in list(str(int(input('>>>')))):
    s += int(i)
    p *= int(i)
print(f'Sum: {s}, Pro: {p}.')
