import fire

def binary_search(list, valor: int):
    
    ini = 0
    fim = len(list) - 1

    while (ini <= fim):
        meio = (ini+fim) // 2
        chute = list[meio]

        if chute == valor:
            return meio
        elif chute > valor:
            fim = meio - 1
        else:
            ini = meio + 1
    
    return None