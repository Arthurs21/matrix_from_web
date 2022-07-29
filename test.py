a = input('Введите путь')
f = open(a)
sp = []
sp_end = []
value = 1
for line in f:
    if value % 2 == 0:
        for i in line.split():
            sp.append(i)
    value += 1
for j in sp:
    if j != '|':
        sp_end.append(j)

print(sp_end)
