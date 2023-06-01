szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
TSzavak = []
for szo in szavak:
    if szo[0] == "T":
       TSzavak.append(szo)
    if szo[0] == "t":
           TSzavak.append(szo)
print(TSzavak)