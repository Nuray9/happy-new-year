f = open('input.txt', 'rt')

instr = f.read()
i = 0

san_x = 0
san_y = 0
rob_x = 0
rob_y = 0

coordin = ['0,0']

while i < len(instr):
    if instr[i] == '>':
        if i % 2 == 0:
            san_x += 1
        else:
            rob_x += 1
    if instr[i] == '<':
        if i % 2 == 0:
            san_x -= 1
        else:
            rob_x -= 1
    if instr[i] == 'v':
        if i % 2 == 0:
            san_y -= 1
        else:
            rob_y -= 1
    if instr[i] == '^':
        if i % 2 == 0:
            san_y += 1
        else:
            rob_y += 1

    if i % 2 == 0:
        coordin.append(str(san_x) + ',' + str(san_y))
    else:
        coordin.append(str(rob_x) + ',' + str(rob_y))

    i += 1

print(coordin)
a = len(set(coordin))
print(a)

o = open('output2.txt', 'w')
o.write(str(len(set(coordin))))
o.close()
