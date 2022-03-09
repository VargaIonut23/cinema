def sort(lista, lista1, sorted: bool):
    n = len(lista1)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sorted is False:
                if lista1[j] > lista1[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
            else:
                if lista1[j] < lista1[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
    return lista
