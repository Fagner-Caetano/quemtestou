# Validação se o n° é par ou impar

def VerificarParImpar(numero):
  if numero % 2 == 0:
    return f"{numero} eh um numero par."
  else:
    resultado = f"{numero} eh um numero impar."
    return resultado

NumeroTeste = 10
resultado = VerificarParImpar(NumeroTeste)
print(resultado)

numero_teste_2 = 7
resultado_2 = VerificarParImpar(numero_teste_2)
print(resultado_2)

import os