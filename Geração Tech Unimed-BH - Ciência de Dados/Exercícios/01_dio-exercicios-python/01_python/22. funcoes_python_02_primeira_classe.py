def somar (a, b):
	return a + b

def subtrair (a,b):
	return a - b

def multiplicacao (a,b):
    return a * b

def exibir_resultado(a,b,funcao):
	resultado = funcao(a,b)
	print(f"O resultado da operação e = {resultado}")
exibir_resultado(10,10,somar)
exibir_resultado(10,10,subtrair)
exibir_resultado(10,10,multiplicacao)

# Também podemos atingir esse comportando atribuindo à uma variável, sendo considerar um objeto de primeira classe

op = somar
print (op(1,23))