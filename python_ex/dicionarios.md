# Dicionários

## Básico

```python
In [1]: d = {'pais': 'Marrocos', 'temperatura': 32.9}

In [2]: 'chuva' in d
Out[2]: False

In [3]: 'Marrocos' in d.values()
Out[3]: True

In [4]: d.get('chuva')

In [5]: print(d.get('chuva'))
None

In [6]: print(d.get('chuva', 'Não'))
Não
```

Retornando chaves e valores.

```python
In [7]: d.keys()
Out[7]: dict_keys(['temperatura', 'pais'])

In [8]: d.values()
Out[8]: dict_values([32.9, 'Marrocos'])

In [9]: d.items()
Out[9]: dict_items([('temperatura', 32.9), ('pais', 'Marrocos')])
```

Adicionando uma nova chave

```python
In [10]: d['capital'] = 'Rabat'

In [11]: d
Out[11]: {'capital': 'Rabat', 'pais': 'Marrocos', 'temperatura': 32.9}
```

Transformando dicionários em tuplas

```python
In [12]: k = tuple(d.keys())

In [13]: v = tuple(d.values())

In [14]: i = tuple(d.items())

In [15]: k
Out[15]: ('temperatura', 'capital', 'pais')

In [16]: v
Out[16]: (32.9, 'Rabat', 'Marrocos')

In [17]: i
Out[17]: (('temperatura', 32.9), ('capital', 'Rabat'), ('pais', 'Marrocos'))
```

Deletando um par

```python
In [18]: del d['capital']

In [19]: d
Out[19]: {'pais': 'Marrocos', 'temperatura': 32.9}
```

Transformando uma tupla num dicionário

```python
In [20]: dict(i)
Out[20]: {'capital': 'Rabat', 'pais': 'Marrocos', 'temperatura': 32.9}
```

## Matriz esparsa implementada como dicionário

Matriz esparsa é uma estrutura que só armazena os valores que existem na matriz.

```python
dim = 6, 12
mat = {}
```

Tuplas são imutáveis. Cada tupla representa uma posição na matriz.

```python
mat[3, 7] = 3
mat[4, 6] = 5
mat[6, 3] = 7
mat[5, 4] = 6
mat[2, 9] = 4
mat[1, 0] = 9
```

Método `get(chave, valor)` retorna o valor da chave no dicionário ou se a chave não existir, retorna o segundo argumento.

```python
for lin in range(dim[0]):
    for col in range(dim[1]):
        print(mat.get((lin, col), 0), end=' ')
    print()
```

**Saída**:

```python
0 0 0 0 0 0 0 0 0 0 0 0 
9 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 4 0 0 
0 0 0 0 0 0 0 3 0 0 0 0 
0 0 0 0 0 0 5 0 0 0 0 0 
0 0 0 0 6 0 0 0 0 0 0 0 
```
