entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])


icm = float((distancia/(diametro1 + diametro2)))

resultado = '{:0.2f}'.format(icm)

print(resultado)