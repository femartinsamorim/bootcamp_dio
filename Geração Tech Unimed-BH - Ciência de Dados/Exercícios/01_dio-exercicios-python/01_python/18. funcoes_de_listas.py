### LISTA | ACESSO DIRETO | INDICES NEGATIVOS | LISTAS ANINHADAS ###

frutas = ["uva","laranja","maça"]
frutas2 = []
print (frutas)
print (frutas2)
letras = list("Python")
print (letras)
print(letras[0])
numeros_1 = list(range(20))
print (numeros_1)
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro[-2])

#Matriz

matriz = [
        [1,"a",2],
        ["b",3,4],
        [5,6,"c"]
    ]

print(matriz[0])
print(matriz[1][0])
print(matriz[-1][-1])

### FATIAMENTO ###

lista2 = ["F","E","L","I","P","E"]
print (lista2[:1])
print (lista2[1:])
print (lista2[:])
print (len(lista2[:]))
print (lista2[2:5])
print (lista2[::2])
print (lista2[::-1])

### ITERAR LISTAS ###

carros = ["Gol","Celta","Palio","HB20","Focus","Civic","Hilux"]

for carro in carros:
    print (carro)
    
for carro1 in carros:
    print(f"Essa lista possui o carro {carro1}")
    
### FUNÇÃO ENUMERATE ###

for indice, carro in enumerate(carros):
	print (f"{carro}: {carro}")

### COMPREENSÃO DE LISTAS ###

# Filtro 01
numeros_2 = [1, 30, 21, 2, 9, 65, 34]
pares_2 = []
for numero_2 in numeros_2:
	if numero_2 % 2 == 0:
	    pares_2.append(numero_2)
print(pares_2)

# Filtro 02
numeros_3 = [1, 30, 21, 2, 9, 65, 34, 55, 100, 52, 60]
pares_3 = [numero_3 for numero_3 in numeros_3 if numero_3 % 2 == 0]
print(pares_3)

# Modificando valores 01
numeros_4 = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero_4 in numeros_4:
	quadrado.append(numero_4 ** 2)
print(quadrado)

# Modificando valores 02
numeros_5 = [1, 30, 21, 2, 9, 65, 34]
quadrado_5 = [numero_5 ** 2 for numero_5 in numeros_5]
print(quadrado_5)

### METODOS DA CLASSE LIST ###

# Append
lista_2 = []
lista_2.append(1)
lista_2.append("python")
lista_2.append([10, 30, 20])	
print(lista_2)

# Clear
lista_3 = [1,"python",[40, 30, 20],"Pratos",1996]
print(lista_3)
lista_3.clear()
print(lista_3)

# Copy
lista_4 = [1,"python",[40, 30, 20],"House Vs Hurricane"]
print(lista_4)
l4cop = lista_4.copy()
print(l4cop)
print(id(l4cop), id(lista_4))
l4cop.append("House of Cards")
print(l4cop)

# Count
cores = ["vermelho","azul","verde","azul"]
print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# Extend
linguagens = ["python","java","c"]
print (linguagens)
linguagens.extend(["java","csharp","JS"])
print(linguagens)

# Index
linguagens_2 = ["python","java","c","java","csharp"]
print(linguagens_2.index("java"))
print(linguagens_2.index("python"))

# Pop
linguagens_3 = ["python","java","c","java","csharp"]
print(linguagens_3)
linguagens_3.pop()
print(linguagens_3)
linguagens_3.pop()
print(linguagens_3)
linguagens_3.pop()
print(linguagens_3)
linguagens_3.pop(0)
print(linguagens_3)

# Remove
linguagens_4 = ["python","java","c","java","csharp"]
linguagens_4.remove("c")
print(linguagens_4)

# Reverse
linguagens_5 = ["python","java","c","java","csharp","JS","PHP"]
print(linguagens_5)
linguagens_5.reverse()
print(linguagens_5)

# Sort
linguagens_6 = ["python","java","c","java","csharp","HTML","c++",]
print(linguagens_6)
linguagens_6.sort() #OBS.: Ordenação padrão por ordem alfabética
print(linguagens_6)
linguagens_6.sort(reverse=True) #OBS.: Ordenação decrescente
print(linguagens_6)
linguagens_6.sort(key=lambda x: len(x)) #OBS.: Ordenação por tamanho (len) da palavra de forma crescente, onde "x" é o argumento, ou seja, cada item da lista
print(linguagens_6)
linguagens_6.sort(key=lambda x: len(x), reverse=True) #OBS.: Mesmo exemplo de cima, mas de forma decrescente
print(linguagens_6)

# len
linguagens_7 = ["python","java","c","java","csharp"]
print(len(linguagens_7))

# Sorted: A diferença dele para o "sort" é que ele é tratado como uma função
