sq = 0

with open("input1.txt") as f:
    for i in f.readlines():
        l, w, h = list(map(int, list(i.split('x'))))
        s1, s2, s3 = l * w, w * h, l * h
        a=min(s1, s2, s3)
        s=(2 * s1 + 2 * s2 + 2 * s3) + a
        sq += s

output = open('output1.txt','w')
output.close()



        
