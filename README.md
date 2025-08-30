# MaxMin Select - Algoritmo de Seleção Simultânea #

## Descrição do Projeto

Este projeto implementa o algoritmo **MaxMin Select** utilizando a técnica de **divisão e conquista** para encontrar simultaneamente o maior e menor elemento de um array de números. O algoritmo é mais eficiente que uma busca linear simples, reduzindo o número de comparações necessárias.

### Lógica do Algoritmo

O algoritmo MaxMin Select funciona dividindo recursivamente o problema em subproblemas menores:

1. **Divisão**: O array é dividido ao meio até chegar aos casos base
2. **Conquista**: Os subproblemas são resolvidos recursivamente
3. **Combinação**: Os resultados são combinados para encontrar o min/max global

## Como Executar o Projeto

### Pré-requisitos
- Python 3.6 ou superior instalado

### Execução
1. Clone ou baixe o repositório
2. Navegue até o diretório do projeto
3. Execute o comando:
```bash
python main.py
```

## Explicação do Código (Linha a Linha)

### Função Principal: `max_min_select(arr, left, right)`

```python
def max_min_select(arr, left, right):
```
- **Linha 1**: Define a função com parâmetros: array, índice inicial e final

```python
if left == right:
    return arr[left], arr[left]
```
- **Linhas 2-3**: **Caso base 1** - Se há apenas um elemento, ele é tanto o mínimo quanto o máximo

```python
if right == left + 1:
    if arr[left] < arr[right]:
        return arr[left], arr[right]
    else:
        return arr[right], arr[left]
```
- **Linhas 4-8**: **Caso base 2** - Se há dois elementos, compara e retorna (min, max)

```python
mid = (left + right) // 2
```
- **Linha 9**: **Divisão** - Calcula o ponto médio para dividir o array

```python
min1, max1 = max_min_select(arr, left, mid)
min2, max2 = max_min_select(arr, mid + 1, right)
```
- **Linhas 10-11**: **Conquista** - Chamadas recursivas para as duas metades do array

```python
return min(min1, min2), max(max1, max2)
```
- **Linha 12**: **Combinação** - Compara os resultados das duas metades e retorna o mínimo e máximo globais

## Relatório Técnico

### 1. Análise da Complexidade pelo Método de Contagem de Operações

#### Contagem de Comparações

O algoritmo MaxMin Select realiza comparações em diferentes cenários:

**Casos Base:**
- **1 elemento**: 0 comparações
- **2 elementos**: 1 comparação

**Caso Recursivo:**
- Para cada divisão, são feitas 2 comparações na etapa de combinação:
  - `min(min1, min2)` → 1 comparação
  - `max(max1, max2)` → 1 comparação

#### Análise Detalhada

Para um array de tamanho **n**:

1. **Profundidade da Recursão**: ⌊log₂(n)⌋ níveis
2. **Número de Subproblemas**: Em cada nível k, há 2^k subproblemas
3. **Comparações por Nível**: 
   - Nível 0: 2^0 × 2 = 2 comparações
   - Nível 1: 2^1 × 2 = 4 comparações
   - Nível k: 2^k × 2 comparações

**Total de Comparações:**
```
T(n) = 2 × (2^0 + 2^1 + 2^2 + ... + 2^⌊log₂(n)⌋-1)
T(n) = 2 × (2^⌊log₂(n)⌋ - 1)
T(n) ≈ 2n - 2 comparações
```

**Complexidade Temporal**: **O(n)**

### 2. Análise da Complexidade pelo Teorema Mestre

#### Recorrência do MaxMin Select
```
T(n) = 2T(n/2) + O(1)
```

#### Identificação dos Parâmetros

**Passo 1**: Identificar valores na fórmula T(n) = a·T(n/b) + f(n)
- **a = 2** → Número de chamadas recursivas (duas metades)
- **b = 2** → Fator de divisão do problema (divisão ao meio)
- **f(n) = O(1)** → Custo das operações fora da recursão (comparações constantes)

**Passo 2**: Calcular log_b(a)
```
p = log_b(a) = log₂(2) = 1
```

**Passo 3**: Determinar o caso do Teorema Mestre

Comparando f(n) com n^p:
- f(n) = O(1) = O(n^0)
- n^p = n^1 = n

Como **0 < 1**, temos **f(n) = O(n^p-ε)** onde ε = 1

**Resultado**: Enquadra-se no **Caso 1** do Teorema Mestre

**Passo 4**: Solução Assintótica
```
T(n) = Θ(n^p) = Θ(n^1) = Θ(n)
```

#### Conclusão
Ambos os métodos confirmam que o algoritmo MaxMin Select possui **complexidade temporal O(n)**, sendo mais eficiente que uma busca ingênua que faria 2n-1 comparações.

## Vantagens do Algoritmo

1. **Eficiência**: Reduz o número de comparações de 2n-1 para aproximadamente 1.5n
2. **Elegância**: Utiliza o paradigma dividir-para-conquistar de forma clara
3. **Escalabilidade**: Mantém complexidade linear mesmo para arrays grandes
4. **Simplicidade**: Implementação recursiva intuitiva e fácil de entender

## Exemplo de Execução

```
Array original: [3, 1, 9, 7, 2, 8, 4, 6, 5]
Menor elemento: 1
Maior elemento: 9
```