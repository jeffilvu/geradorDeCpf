import random

while True:
    resposta = ''
    noveDigitos = ''
    for i in range(9):
        noveDigitos += str(random.randint(0, 9))

    multp = 10
    somaDigitos = 0
    primeiroDigito = 0
    segundoDigito = 0

    for digito in noveDigitos:
        digito = int(digito)
        digitoMultiplicado = digito*multp
        multp = multp-1
        somaDigitos = somaDigitos + digitoMultiplicado
        somaDigitosMultiplicado = somaDigitos * 10
        primeiroDigito = somaDigitosMultiplicado % 11

    if primeiroDigito > 9:
        primeiroDigito = 0

    primeiroDigito = str(primeiroDigito)
    dezDigitos = noveDigitos + primeiroDigito
    multp = 11
    somaDigitos = 0

    for digito in dezDigitos:
        digito = int(digito)
        digitoMultiplicado = digito*multp
        # print(f'{digitoMultiplicado}')
        multp = multp-1
        somaDigitos = somaDigitos + digitoMultiplicado
        somaDigitosMultiplicado = somaDigitos * 10
        segundoDigito = somaDigitosMultiplicado % 11

    if segundoDigito > 9:
        segundoDigito = 0

    cpfCalculado = noveDigitos + str(primeiroDigito) + str(segundoDigito)
    print(f"{cpfCalculado}\n")

    while resposta != 'C' and resposta != 'S':
        resposta = input("Envie [C] para gerar outro CPF ou [S] para sair.\n")
        resposta = resposta.upper()

    if resposta == 'C':
        continue
    elif resposta == 'S':
        break
