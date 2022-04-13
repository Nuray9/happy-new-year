input= open('input.txt').read()

k = 0

for i in input:
    if i  == '(':
        k+= 1
    else:
        k += -1

output = open('output1.txt','w')
output.write(str(k))

output.close()

