import hashlib

with open('input.txt','r', encoding='utf-8') as f:
    origin = f.readline()

i = 0
while True:
    k = origin + str(i)
    r = hashlib.md5(k.encode())
    hexdigit = str(r.hexdigest())

    if not ('00000' in ''.join(hexdigit[0:5].split())):
        i += 1
    else:
        break

with open("output1.txt", "w") as f:
    print(i, file = f)
