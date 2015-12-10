# Tuplas

## Básico

```python
>>> t = ('asd', 'fg')
>>> t
('asd', 'fg')
>>> t + ('qwert', 'poiuy')  # is a new tuple
('asd', 'fg', 'qwert', 'poiuy')
>>> tuple('abcdefghij')
('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
>>> tuple([1, 2, 3])
(1, 2, 3)
>>> ('A', 'B') + t
('A', 'B', 'asd', 'fg')
>>> ('A',)
('A',)
```

## Tuplas vs Listas

### Tuplas podem ser convertidas em listas

```python
>>> lista = [1, 2, 3]
>>> lista
[1, 2, 3]
>>> tupla = tuple(lista)
>>> tupla
(1, 2, 3)
```

### Listas podem ser convertidas em tuplas


```python
lista = list(tupla)
```

### Podemos desempacotar os elementos de uma tupla através de atribuição

```python
>>> tupla = (1, 2, 3)
>>> a, b, c = tupla
>>> print(a, '+', b, '+', c, '=', a+b+c)
1 + 2 + 3 = 6
```
