inp =input ("Escreva uma palavra")
lista=[]
i = len(inp)
while i > 0: 
    lista += inp[i-1]
    i = i - 1 # decrement index
aux= "".join(lista)
print(aux)
