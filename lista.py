fp1 = open("DGE.txt","r")
fp2 = open("PADRONACTIVOS.csv","r")
output = open("salida.txt", "w")

dge = fp1.readlines()
fp1.close()

padron = fp2.readlines()    
fp2.close()

pop = []
for j in range(len(padron)):
    padron[j] = padron[j].split(";")
    if padron[j][6] == "":
        pop.append(j)

pop.sort(reverse = True)

for i in range(len(pop)):
    padron.pop(pop[i])

padron.pop(0)

dgepop = []
padronpop = []
for i in range(len(dge)):
    dni = dge[i][7:15]
    for j in range(len(padron)):
        check = padron[j][6].replace(".", "")
        check = check.replace(",", "")
        if dni == check:
            padronpop.append(j)
            dgepop.append(i)
            break

print >> output

dgepop.sort(reverse = True)
for i in range(len(dgepop)):
    dge.pop(dgepop[i])

padronpop.sort(reverse = True)
for i in range(len(padronpop)):
    padron.pop(padronpop[i])

dgenuevo = [i for i in dge if i[44:47] == "100"]
dgeignore = [i for i in dge if i[44:47] == "000"]
for i in range(len(dgenuevo)):
    print >> output, "HAY QUE CARGAR: " + dgenuevo[i][18:41] + " en Padron, DNI: " + dgenuevo[i][7:15]

print >> output

padronnuevo = [i for i in padron if i[1] == "a"]
padronignore = [i for i in padron if i[1] == "A"]
for i in range(len(padronignore)):
    print >> output, "REVISAR: " + padronignore[i][3] + ", DNI: " + padronignore[i][6] + "."

print >> output

for i in range(len(dgeignore)):
    print >> output, "No encontre: " + dgeignore[i][18:41].strip() + " en Padron, pero no paga"


print >> output

for i in range(len(padronnuevo)):
    print >> output, "No encontre: " + padronnuevo[i][3] + ", DNI: " + padronnuevo[i][6] + " en DGE, pero es el primer mes."

print >> output

output.close()