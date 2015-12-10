# Listas

## Dicas

```python
lista = ['um', 'dois', 'tres']
```

### Ex: podemos imprimir enumerado

```python
In [2]: for i, lista in enumerate(lista):
   ...:     print(i + 1, '-->', lista)
   ...:     
1 --> um
2 --> dois
3 --> tres
```

O iterador `enumerate()` retorna uma tupla de dois elementos a cada iteração: um número sequencial e um item da sequência correspondente.

### Ex: a lista contém o método `pop()`, que facilita a implementação de filas e pilhas:

**Filas**

Em filas, o primeiro item é o primeiro a sair.

```python
In [3]: lista = ['um', 'dois', 'tres']

In [4]: print('lista:', lista)
lista: ['um', 'dois', 'tres']

In [5]: # A lista vazia é avaliada como falsa

In [6]: while lista:
   ...:     # pop(0) remove e retorna o primeiro item
   ...:     print('Saiu', lista.pop(0))
   ...:     
Saiu um
Saiu dois
Saiu tres
```

**Pilhas**

Em pilhas, o primeiro item é o último a sair.

Mais itens na lista

```python
In [7]: lista += ['quatro', 'cinco', 'seis']

In [8]: print('lista:', lista)
lista: ['quatro', 'cinco', 'seis']

In [9]: while lista:
   ...:     # pop() remove e retorna o último item
   ...:     print('Saiu', lista.pop())
   ...:     
Saiu seis
Saiu cinco
Saiu quatro
```

