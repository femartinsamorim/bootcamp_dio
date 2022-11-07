#salario = 2000
#def salario_bonus(bonus):
#	global salario
#	salario += bonus
#	return salario
#salario_com_bonus = salario_bonus(500)
#print(salario_com_bonus)

# EXEMPLO 02:

#salario = 2000
#def salario_bonus(bonus, lista):
#	global salario
#	lista.append(2)
#	salario += bonus
#	return salario
#lista = [1]
#salario_com_bonus = salario_bonus(500, lista)
#print(salario_com_bonus)
#print(lista)

# A lista é um objeto imutável, e por ele ser isso , 
# tudo que fazermos de operação dentra da lista será refletido para objeto de fora, 
# para isso não acontecer a dica é usar o método copy

salario = 2000

def salario_bonus(bonus, lista):
	global salario
	lista_aux = lista.copy()
	lista_aux.append(2)
	print(f"lista auxiliar={lista_aux}")
	salario += bonus
	return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)