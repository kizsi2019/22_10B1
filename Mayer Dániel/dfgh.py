
l = [2,6,9,7,41,4]

def max(l):
    lmao = l[0]
    for i in range(1,len(l)):
        if l[i] > lmao:
            lmao = l[i]
    return lmao

print(max(l))