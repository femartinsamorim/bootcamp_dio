def salvar_carro(marca,modelo,ano,placa):

	print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

#salvar_carro("Fiat","Palio",1999,"ABC-1234")
# # Primeira Forma: Desvantagem é que pode ocorrer troca do valores.
#salvar_carro(marca="Fiat",modelo="Palio",ano=1999,placa="ABC-1234")
# Segunda Forma: Nomeado não terá problema em troca dos valores, mas se mudar o nome da variável pode dar problema
salvar_carro(**{"marca":"Fiat","modelo":"Palio","ano":1999,"placa":"ABC-1234"})
# Terceira Forma: Usando "**" estamos informando que vamos usar um dicionário para a função "salvar_carro", convertando para ficar semelhante ao modelo acima.