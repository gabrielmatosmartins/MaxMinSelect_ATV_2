def max_min_select(arr, left, right):
    """
    Algoritmo MaxMin Select usando divisão e conquista.
    
    Args:
        arr: Lista de números
        left: Índice inicial do subarray
        right: Índice final do subarray
    
    Returns:
        tuple: (menor_elemento, maior_elemento)
    """
    if left == right:
        return arr[left], arr[left]

    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    mid = (left + right) // 2
    min1, max1 = max_min_select(arr, left, mid)
    min2, max2 = max_min_select(arr, mid + 1, right)
    return min(min1, min2), max(max1, max2)


def main():
    """Função principal para testar o algoritmo MaxMin Select."""
    arr = [3, 1, 9, 7, 2, 8, 4, 6, 5]
    
    print("=== Algoritmo MaxMin Select ===")
    print(f"Array original: {arr}")
    print(f"Tamanho do array: {len(arr)}")
    
    min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
    
    print(f"\nResultados:")
    print(f"Menor elemento: {min_val}")
    print(f"Maior elemento: {max_val}")
    print("\n=== Testes Adicionais ===")
    
    test_arrays = [
        [5],
        [3, 7],
        [10, 5, 8, 2],
        [15, 3, 9, 1, 12, 6, 4, 11, 8, 2, 7, 14, 13, 5, 10]
    ]
    
    for i, test_arr in enumerate(test_arrays, 1):
        min_val, max_val = max_min_select(test_arr, 0, len(test_arr) - 1)
        print(f"Teste {i}: {test_arr}")
        print(f"  Min: {min_val}, Max: {max_val}")


if __name__ == "__main__":
    main()