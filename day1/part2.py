k = 0

with open("input.txt") as f:
    st = ''.join(f.readlines())


for i in range(len(st)):
    if k >= 0:
        if st[i] == "(":
            k += 1
        else:
            k -= 1
    else:
        k = i
        break


with open("output2.txt", "w") as f:
    print(k, file=f)
