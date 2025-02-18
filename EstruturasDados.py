# LIST
'''
lista = ["Maçã", "Pera", "Laranja"]

lista.append("Cereja")
lista.insert(2,"Fruta")
lista.pop()

print(lista)
'''

# TUPLE
amigos = ("Ana", "Rita", "Jorge")

lista = list(amigos)

print(lista)

lista.remove("Ana")

print(lista)

# SET
'''
flores = {"Rosa", "Tulipa", "Lotus"}

flores.add("Jasmin")

print(len(flores))
'''

# DICIONARIO
calendario = {1:"Jan", 2:"Fev", 3:"Mar", 4:"Abr", 5:"jun"}
z = calendario[1]
print(z)

calendario[4] = "Maio"
print(calendario)

calendario.update({5: "Mai"})
print(calendario)

