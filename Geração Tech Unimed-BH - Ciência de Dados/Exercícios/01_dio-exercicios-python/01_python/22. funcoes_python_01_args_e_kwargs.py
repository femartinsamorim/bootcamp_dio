def exibir_poema(data_extenso,*lista, **dicionario):
	texto = "\n".join(lista)
	meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
	mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
	print(mensagem)
 
exibir_poema(
    "\nDomingo, 09 de Outubro de 2022",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Abraços e tchau!",
    autor="Tim Peters",
    ano=1999
    )

#def exibir_poema(data_extenso,*args, **kwargs):
#	texto = "\n".join(args)
#	meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
#	mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
#	print(mensagem)