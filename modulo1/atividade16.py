def insertion_sort(l):
    for ponteiro in range(len(l)):
        j = ponteiro + 1
        while j - 1 >= 0 and j < len(l) and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1

    return l

lista = [12, 11, 13, 5, 6]
nova_lista = insertion_sort(lista)
print(nova_lista)