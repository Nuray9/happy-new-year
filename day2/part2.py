k = 0

with open("input.txt") as f:
    for i in f.readlines():
        l, w, h = list(map(int, list(i.split('x'))))
        r = min(2 * l + 2 * h, 2 * w + 2 * h, 2 * l + 2 * w)
        b = l * w * h
        k += (r + b)

with open("output1.txt", "w") as f:
    print(k, file=f)
    
