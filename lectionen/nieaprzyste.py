def nieparzyste(lista):
    nieparzyste = []
    for element in lista:
        if element % 2:
            nieparzyste.append(element)
    
    print(*nieparzyste, sep=", ")
    print("Jest ich:", len(nieparzyste))

lista = [3, 12, 8, 5, 99, 67]
nieparzyste(lista)