lista1 = []
lista2 = []

for i in range(3):
    valor = int(input("Digite um valor para a lista 1: "))
    lista1.append(valor)

for i in range(3):
    valor = int(input("Digite um valor para a lista 2: "))
    lista2.append(valor)

lista3 = lista1 + lista2

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)