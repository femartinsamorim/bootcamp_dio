from cgi import print_arguments


nome = "feLIpe"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " Olá mundo!  "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

centralizacao = "Python"
print (centralizacao.center(30, "*"))

juncao = "Python"
print(",".join(juncao))

for letra in juncao:
    print(letra, end=",")
print()