# Resumen
Se busca tener una referencia de lo que mas se suele usar en python

## OPERACIONES

```
# Suma  +
# Resta -
# Multiplicación *
# División /
# Potencia **
# Divisón entera //
# Módulo %
```
##  OPERADORES
```
# Igual ==
# Diferente !=
# Menor <
# Mayor >
# Menor o igual <=
# Mayor o igual >=
# Rango  a en (b:c)  b <= a <= C

# Y  and
# o  or
# No not
```



## TIPOS

- int - números enteros 
`print(type(5))  # <class 'int'>`
- float - reales
`print(type(3.5))  # <class 'float'>`
- complex - complejos
`print(type(3 + 2j))  # <class 'complex'>`
- booleano
`print(type(True))  # <class 'bool'>`

- string - caracteres
`
print(type("Hola"))  # <class 'str'>
`
```
Dentro de las comillas se pueden añadir caracteres
especiales escapándolos con ‘\’, como ‘\n’ ó ‘\t’
– 'Help! Help! I\'m being repressed!'
– “Help! Help! I'm being repressed!”
```
___

## Manejo de cadenas
Las cadenas empiezan en la posición `0` y terminan en la `(len(x) - 1)`

O desde el final empiezan en la posición `-1` y terminan en la posición `-(len(x))`

###operador de corte  ` x[i:j:k]`
- `i` es la posición inicial; si se omite es `0`, el inicio
- `j` es la posición final; si se omite es el `len(x)`, el final
- `k` es el salto de las siguientes posiciones consideradas luego de `i: i, i+k, i+2k ..., j`
- si `k` se omite es `1`; puede ser negativo entonces va en sentido inverso

```
x = 'Hola mundo.'
print(x)         # Hola mundo.
print(x[2:])     # la mundo.
print(x[:4])     # Hola
print(x[1:9:3])  # o n
print(x[::-1])   # .odnum aloH
```


### len(x) 
largo de la cadena x 
`print(len(x))  # 11`
### str.lower(x) 
pasa la cadena x a minúsculas
`print(x.lower())  # hola mundo.`
### str.upper(x)  
pasa la cadena a mayúsculas
`print(x.upper())  # HOLA MUNDO.`
### str.replace(“a”,”b”) 
Sustituye todas las # ocurrencias de “a” con la letra “b
`print(x.replace("o", "0"))  # H0la mund0.`
### str(xxx) 
castea xxx a string
`print(type(str(5)))  # <class 'str'>`
___

## Entrada `input()`
 devuelve el valor ingresado por teclado; siempre es texto

`var = input("Ingrese un valor: ")`
___

## Asignación
- ### Simple `<var> = <expr>`
- ### Simultanea `<var1>, <var2>, ... = <expr1>, <expr2>, ...`

``` 
a, b = 1, 2
print(a, b)  # 1 2 
```

## Salida en Pantalla
- ###  Usando `str.format()`
```
print('Somos los {0} quienes decimos ¡{1}!'.format('caballeros', 'No'))  # Somos los caballeros quienes decimos ¡No!
print("{0:b} {1:o} {2:d} {3:x}".format(10, 10, 10, 10))  # 1010 12 10 a
```
`b`:binario; `o`:octal; `d`: decimal; `x`:hexadecimal;
- ### Usando `f-String` (es la forma recomendada)
```
nombre = "Sergio"
edad = 53
print(f"Hola {nombre}, tu edad es {edad}")  # Hola Sergio, tu edad es 53
 ```
___

# Estructuras de control

### IF
```
  if <condición>:
    acciones
  elif <condición>:      opcional
    acciones
  else:                  opcional
    acciones
```

### WHILE
Repite las acciones hasta cumplir la condición
```
  while <condición>:
    acciones
```

### FOR
```
  for <variable> in <serie de valores>
    acciones
```
```
  for x in range(n1,n2,salto):
```

La función `range` genera la secuencia de valores enteros del intervalo `(n1, n2)`; `n1` es opcional, si se omite es `0`
  Dicho de otra forma, va de `n1` a `n2-1` en incrementos dados por `salto`, que si se omite es `1`
  
-  `break` se utiliza para romper un ciclo
___


# Funciones

```
def nombre_funcion(lista_de_parametros):
    sentencias
    return(lista_de_salidas)
```    
En la lista de parámetros se puede consignar un valor por defecto para c/u
``` 
def funcion_ejemplo(par1, par2=1):
    return(sal1,sal2)
```

Se invoca con el nombre de la función
``` 
funcion_ejemplo(1) 
```
Para este caso par2 toma el valor por defecto

Cuando colocamos un `*` adelante del parámetro de una función, estamos indicando que 
se va a recibir un número indeterminado de parámetros. 
Además esos parámetros se recibirán en forma de tupla.
```
def sumaNumeros(*numeros):
     total = 0
     for n in numeros:
          total =  total + n
     print(total)
sumaNumeros(1, 5, 7)  # 13     
```
___

# Listas

Es un tipo de colección ordenada que nos permite agrupar elementos de cualquier tipo.
Se declaran encerrando los valores entre `[]` separados por `,`

```
lista = ["Elemento_1", "Elemento_2"]
print(lista)  # ['Elemento_1', 'Elemento_2']
print(type(lista))  # <class 'list'>
```

Para acceder a los elementos de una lista se puede hacer a través de su índice
```
print(lista[1])  # Elemento_2
```
Tener en cuenta que el primer índice de una lista es el `0` y el ultimo es `(largo(lista)– 1)`
```
print(len(lista))  # 2
```
Igual que con los string se puede acceder desde el final, va de `-1` a `-(largo(lista))`
```
print(lista[-1])  # Elemento_2
```

## Listas anidadas (simil matrices)
```
matriz = [[11, 12], [21, 22]]
```
se acceded con `[][]`
```
print(matriz[0][1])  # 12
```

## Particionado de listas 
Podemos realizarlo de igual forma que con los string
```
lista_larga = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista_larga[1:8:2])  # [1, 3, 5, 7]
```

## Operadores de listas  
El operador `+` concatena y el `*` repite

## Funciones de listas

### len
Retorna el largo de la lista - `len(lista)`  
```
print(len(lista_larga))  # 10
```

### append
Agrega un elemento a la lista  - `lista.append`
```
lista.append("Elemento_3")
print(lista)  # ['Elemento_1', 'Elemento_2', 'Elemento_3']
```

### insert
Inserta el valor `b` en la posición `a` - `lista.insert(a,b)`
```
lista.insert(1, "Elemento_1,5")
print(lista)  # ['Elemento_1', 'Elemento_1,5', 'Elemento_2', 'Elemento_3']
```

### count
Contar las ocurrencias del elemento `a` - `lista.count(a)`
```
otra_lista = [1, 3, 3, 6, 1, 4, 7, 8, 1]
print(otra_lista.count(1))  # 3
```

### in
Devuelve si el elemento está o no en la lista
```
print(1 in otra_lista)  # True
```

### index
Retorna la posicion en la lista del elemento a, si está más de una vez devuelve la primera - `lista.index(a)`
```
print(otra_lista.index(3))  # 1
```

### remove
Elimina un elemento de la lista - `lista.remove`
```
lista = ['Elemento_1', 'Elemento_1,5', 'Elemento_2', 'Elemento_3']
lista.remove("Elemento_1,5")
print(lista)  # ['Elemento_1', 'Elemento_2', 'Elemento_3']
```

### pop
Elimina un elemento de la lista (por defecto el último elemento), y devuelve el valor de dicho elemento.
```
lista = ['Elemento_1', 'Elemento_2', 'Elemento_3']
print(lista.pop())  # Elemento_3 
print(lista) = ['Elemento_1', 'Elemento_2']
```

### sorted
Devuelve una nueva lista ordenada (NO modifica la original)- `sorted(lista)`
```
print(otra_lista)  # [1, 3, 3, 1, 4, 7, 8, 1]
lista_ord = sorted(otra_lista)
print(lista_ord)  # [1, 1, 1, 3, 3, 4, 7, 8]
```

### sort
Ordena la propia lista - `lista.sort()`
```
print(otra_lista)  # [1, 3, 3, 1, 4, 7, 8, 1]
otra_lista.sort()
print(otra_lista)  # [1, 1, 1, 3, 3, 4, 7, 8]
```

### split
Convierte un string `str` en una lista de strings de acuerdo al separador `sep` - `str.split(sep ,maxsplit=-1)`
#### `sep` - carácter de separación
#### `maxsplit` - cantidad máxima de separaciones realizados; -1 que es el defecto implica todas
```
print("Esta es una cadena".split(" "))  # ['Esta', 'es', 'una', 'cadena']
```

### list
Devuelve una lista donde cada elemento de la cadena es un ítem de la lista - `list(cadena)`
```
print(list("Cadena de prueba"))  # ['C', 'a', 'd', 'e', 'n', 'a', ' ', 'd', 'e', ' ', 'p', 'r', 'u', 'e', 'b', 'a']
```

### join
Devuelve un string con los elementos de la lista concatenados (tienen que ser strings)
```
lista = ['1', '2', '4']
print("x".join(lista))  # 1x2x4
```
___

# Tuplas

**La tupla es una secuencia heterogénea de elementos, accesible a través de un índice.
Se declaran encerando los valores entre `()` separados por `,`
Son inmutables y no se pueden modificar**
```
tupla = ("Elem_1", "Elem_2")
print(tupla)  # ('Elem_1', 'Elem_2')
print(type(tupla))  # <class 'tuple'>
```
El acceso a los elementos es por índice igual que listas o strings.

También se puede utilizar con ellos la función len y las referencias por rangos.
___

# Diccionarios
**Colecciones que relacionan clave:valor**

**Como clave podemos utilizar solamente tipos inmutables: números, cadenas, booleanos, tuplas**
```
diccionario = {1: "Uno", 2: "Dos", 3: "Tres"}
print(diccionario)  # {1: 'Uno', 2: 'Dos', 3: 'Tres'}
```

###Se accede por la clave usando `[]`
```
print(diccionario[2])  # Dos
```
### get
Devuelve el valor del diccionario para esa clave - `diccionario.get(clave,[default])`

Si no está devuelve None o lo que se indique
```
diccionario = {1: "Uno", 2: "Dos", 3: "Tres"}
print(diccionario.get(4))  # None
print(diccionario.get(4, "No está"))  # No está
```

### in 
Indica si una clave se encuentra en el diccionario
```
diccionario = {1: "Uno", 2: "Dos", 3: "Tres"}
print(6 in diccionario)  # False
```

### update
Agrega la entrada clave:valor en el diccionario
```
diccionario = {1: "Uno", 2: "Dos", 3: "Tres"}
diccionario.update({6: "Seis"})
print(diccionario)  # {1: 'Uno', 2: 'Dos', 3: 'Tres', 6: 'Seis'}
```

### del
Borra la entrada correspondiente a clave - `del(diccionario[clave])`
```
del (diccionario[3])
print(diccionario)  # {1: 'Uno', 2: 'Dos', 6: 'Seis'}
```

### pop
Borra la entrada correspondiente a clave y retorna su valor asociado - `diccionario.pop(clave)`
```
print(diccionario.pop(6))  # 'Seis'
print(diccionario)  # {1: 'Uno', 2: 'Dos'}
```

### keys
Devuelve una lista desordenada, con todas las claves - `diccionario.keys()`
```
print(diccionario.keys())  # dict_keys([1, 2])
```

### values
Devuelve una lista desordenada, con todos los valores - `diccionario.values()`
```
print(diccionario.values())  # dict_values(['Uno', 'Dos'])
```

### items
Devuelve una lista desordenada con tuplas de dos elementos, 
en las que el primer elemento es la clave y el segundo el valor - `diccionario.items()` 
```
print(diccionario.items())  # dict_items([(1, 'Uno'), (2, 'Dos')])
```

### clear
Elimina todos los elementos del diccionario `diccionario.clear()`

---

# Funciones De Orden Superior

### map - `map (function, sequence[, sequence, ...]) → iterator`
Retorna un iterador donde cada elemento es el resultado de aplicar la función “function” en la
secuencia pasada como parámetro (sequence)

Hay que castear el resultado a lista si se quiere tratar como tal (diferencia con PY 2.x)

Si se pasan como parámetros n secuencias, la función tendrá que aceptar n argumentos.

Si las listas tienen diferentes tamaños, el valor que le llega a la función “function” para las 
posiciones mayores (que no tienen su correspondiente en la otra lista de tamaño menor), será None

```
lista_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_str = list(map(str, lista_num))
print(lista_str)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

```
def sumar(x, y):
    return x + y

lista1, lista2 = range(10), range(10)
lista3 = list(map(sumar, lista1, lista2))
print(lista3)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```


### reduce - `reduce(function, sequence[, initial]) → value`
Se debe importar la librería functools - `import functools`
Se aplica la función “function” de a pares de elementos de una secuencia, hasta dejarla en un
solo valor.

La función retorna un único valor que se construye llamando a la función “function” con los primeros
dos ítems de la secuencia, luego se toma el resultado de estos dos primeros y el siguiente
ítem, y así sucesivamente, de izquierda a derecha.

El parámetro opcional de reduce es un inicializador, esto significa que reduce # evaluará la función de reducción 
comenzando por el valor especificado. Si no se especifica, el inicializador será el 1er. valor de la secuencia
```
import functools
lista = list(range(1, 11))
print(lista)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(functools.reduce(sumar, lista))  # 55
```


### filter - `filter(function or None, sequence) → iterator`

Retorna los ítems de la secuencia para aquellos elementos que hagan verdadera a la función  “function”.

En el caso de que se pase como función None se devuelve la secuencia con los elementos que sean evaluados como verdadero.

El tipo de dato que se devuelve es el mismo que se pasa como parámetro en sequence.
```
def f(x):
    return x % 2 != 0 and x % 3 != 0

print(filter(f, range(2, 25)))  # <filter object at 0x0038E0A0>
print(list(filter(f, list(range(2, 25)))))  # [5, 7, 11, 13, 17, 19, 23]
```
___

# Funciones Lambda
####Las funciones lambda se construyen con: 

1. El operador lambda 
2. Los parámetros de la función separados por comas `,`
3. Luego dos puntos `:` y el código de la función 
```
suma = lambda x, y: x + y
print(suma(3, 56))  # 59
print(list(map(lambda x, y: x + y, list(range(10)), list(range(10)))))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```
___

# Compresion de Listas

Una lista por comprensión consiste de una expresión del tipo ternaria seguida por una cláusula for,
luego cero o más cláusulas for o if
### `[ expresión for item in lista if condición ]`

El resultado será una lista que resulta de evaluar la expresión en el contexto de las cláusulas for e if que sigan.
```
vec = [2, 4, 6]
print([3 * n for n in vec])  # [6, 12, 18]
print([3 * n for n in vec if n > 3])  # [12, 18]
```

Expresión inicial de tipo ternario - `a if condición else c`
Python retorna `a` si la condición es True, sino, retorna `c`.
```
print(["Par" if n % 2 == 0 else "Impar" for n in range(6)])  # ['Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar']
```
---

# Generadores

Un generador es un tipo de función que puede, por así decir, retornar un valor sin terminar del todo su ejecución, 
siendo posible reanudarla después.

Un generador debe incluir la instrucción `yield`. Esto provoca que la función sea clasificada 
como un generador

Cuando se llama a una función normal el intérprete comienza a ejecutar las instrucciones secuencialmente.

Cuando se llama a un generador, la ejecución se detiene después de yield,
se retorna el valor y la función queda suspendida hasta la próxima ejecución

Un ejemplo:
```
def ejemplo_tonto():
    print("Acabo de comenzar")
    yield 1
    print("Continúo")
    yield 2
    return
```

Si intentas ejecutar esta función normalmente, así:
```
>>> r = ejemplo_tonto()
```
verás que no aparece ningún mensaje, lo que indica que la función realmente no comenzó
aún a ejecutarse. 

`r` es un generador y para comenzar a ejecutar realmente esa función
hay que hacer `next()` sobre `r`:
```
>>> r
<generator object ejemplo_tonto at 0x7f6ec11563b8>
>>> resultado = next(r)
Acabo de comenzar
>>> resultado
1
```

#### Cuando el generador se agota (llega a su return), Python genera la excepción `StopIteration:`

Estas funciones permiten extraer valores de una función y almacenarlo (de uno en uno) 
en objetos iterables (que se pueden recorrer),

Sin la necesidad de almacenar Todos a la Vez en memoria Ram

```
def generadorMultiplos7(limite):
     numero = 1
     while numero <= limite:
          yield numero * 7   # Ceder. la instruccion "yield" genera un objeto iterable
          numero = numero + 1
          
obtieneMultiplos7 = generadorMultiplos7(10)    

#  esta bariable en si no se puede imprimir ya que es una funcion.
print(obtieneMultiplos7)  # <generator object generadorMultiplos7 at 0x0000021BB776F5F0>

for n in obtieneMultiplos7:
     print(n)  # 7
                 14
                 21
                 28
                 35
                 42
                 49
                 56
                 63
                 70
```

## next - `next(iterable)`
La función next recibe un objeto iterable y retorna de a uno sus valores en cada invocación.
```
obtieneMultiplos7 = generadorMultiplos7(10) 
print(next(obtieneMultiplos7))  # 7
print(next(obtieneMultiplos7))  # 14
print(next(obtieneMultiplos7))  # 21
```


### Otras forma de generarlas es con listas por comprensión pero usando `()` paréntesis curvos en lugar de rectos
```
def square(x):
    print("Cuadrado de", format(x))
    return x * x


def digit_sum(x):
    print("Suma de", format(x))
    return sum(map(int, str(x)))


numbers = range(1, 5)
squares = [square(n) for n in numbers]
print(squares)
dsums = [digit_sum(n) for n in squares]
for n in dsums:
    print(n)
"""
Cuadrado de 1
Cuadrado de 2
Cuadrado de 3
Cuadrado de 4
[1, 4, 9, 16]
Suma de 1
Suma de 4
Suma de 9
Suma de 16
1
4
9
7
"""
numbers = range(1, 5)
squares = (square(n) for n in numbers)
print(squares)
dsums = (digit_sum(n) for n in squares)
for n in dsums:
    print(n)
"""
<generator object <genexpr> at 0x0025CBF8>
Cuadrado de 1
Suma de 1
1
Cuadrado de 2
Suma de 4
4
Cuadrado de 3
Suma de 9
9
Cuadrado de 4
Suma de 16
7
"""
```

## yield from 

Cuando dentro de un generador se usa yield from, el generador en cuestión se "pausa" 
a la vez que conecta su "salida" por así decir, con la del generador que pongas 
tras yield from. A partir de ese momento, todos los next() se hagan sobre el
generador "externo" llegan directamente al interno, el cual irá retornando sus valores. 

Cuando el generador interno se agote y cause `StopIteration`, se reanudará la 
ejeución del generador externo que estaba pausado.
---


# Archivos

## open - `nombre = open("archivo.dat","modo")`

Abrir un archivo
- La función open toma dos argumentos. El primero es el nombre del archivo y el segundo es el modo.
- Modo puede ser 
     - ***r: read*** 
     - ***w: write*** 
     - ***a: append***
- La función retorna un objeto del tipo file.
- Si se abre de lectura no se puede escribir y si se abre de escritura no se puede leer
```
archivo = open("example.txt", "r")
print(archivo)  # <_io.TextIOWrapper name='example.txt' mode='r' encoding='cp1252'>
```

## close - `nombre.close()`
Cerrar el archivo

Debemos cerrar siempre el archivo al terminar

###Dos formas de asegurarnos que el archivo se cierre correctamente
```
archivo = open("example.txt", "r")
try:
    print(archivo)
finally:
    archivo.close()
```

```
with open("example.txt", "r") as archivo:
    print(archivo)
```

## readline - `archivo.readline()`
Lee una línea.
```
with open("example.txt", "r") as archivo:
    reg = archivo.readline()
    print(reg)  # Primer registro
```

## readlines - `archivo.readlines()`
Devuelve una lista con todas las líneas del archivo.
```
with open("example.txt", "r") as archivo:
    reg = archivo.readlines()
    print(reg)  # ['Primer registro\n', 'Segundo registro\n', 'Tercer registro\n']
```

## read - `archivo.read()`

```
with open("example.txt", "r") as archivo:
    reg = archivo.read()
    print(reg)
"""
Primer registro
Segundo registro
Tercer registro
"""
```

## write - `archivo.write(cadena)`
Escribe un elemento con salto de línea.
```
with open("example.txt", "a") as archivo:
    archivo.write("Cuarto registro\n")
```

## writelines - `archivo.writelines(lista_de_cadenas)`
Escribe un elemento de la lista atrás de otro, sin salto de línea
```
with open("example.txt", "a") as archivo:
    mas_registros = ["Quinto registro", "Sexto registro"]
    archivo.writelines("\n".join(mas_registros))
```

### Ejemplo de ruta
siempre con `/`
```
f = open("/usr/share/dict/words","r") 
```

## Modulo os
El módulo os contiene muchas funciones útiles para el manejo de archivos.

### sep
Abstrae el separador `print(os.sep)  # /`

### makedirs
Crea un directorio

### chdir
Cambia a un directorio

### path.isfile
Dice si un archivo ya existe
```
print(os.path.isfile("example.txt"))
```

### path.isdir
Dice si un directorio ya existe
```
print(os.path.isdir('cat/dog/fish'))
```

## access
Dice cuáles son los permisos sobre el archivo: lectura o escritura

## path.join
Une las rutas con el carácter de separación de directorios que le corresponda al sistema en uso

## makedirs
Crea directorios
este ejemplo usa las dos funciones anteriores para crear 3 carpetas en forma 'cat/dog/fish'
```
os.makedirs(os.path.join('cat','dog','fish'))
```
___

