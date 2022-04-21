import hashlib
f = open("input.txt","r")

Key = f.readline()
res = ""

for i in range(9999999):
    newListKey = [Key]
    
    newListKey.append(i) #добавляем число (i) в конце
    
    mystring = ""
    
    mystring = str(newListKey[0]) + str(newListKey[1])
    
    hash_object = hashlib.md5(mystring.encode()) # Хэш
    
    hash_object = hash_object.hexdigest()

    if hash_object[0:6] == "000000": #Первые 5 чисел нули
        res = mystring[len(Key):]
        print(res)
        break
f.close()
with open('output2.txt','w') as output:
    output.write(str(res))
