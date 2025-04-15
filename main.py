# Validação se o n° é par ou impar


def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"{numero} eh um numero par."
    else:
        resultado = f"{numero} eh um numero impar."
        return resultado


numero_teste = 10
resultado = verificar_par_impar(numero_teste)
print(resultado)

numero_teste_2 = 7
resultado_2 = verificar_par_impar(numero_teste_2)
print(resultado_2)
