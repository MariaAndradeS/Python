def numero_extenso(numero):
    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    especiais = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas = ['zero', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    centenas = ['zero', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

    if numero == 0:
        return 'zero'

    extenso = ''

    if numero // 1000 > 0:
        extenso += unidades[numero // 1000] + ' mil '
        numero %= 1000

    if numero // 100 > 0:
        extenso += centenas[numero // 100] + ' '
        numero %= 100

    if numero >= 10 and numero <= 19:
        extenso += especiais[numero - 10]
    else:
        if numero // 10 > 0:
            extenso += dezenas[numero // 10] + ' '
            numero %= 10

        if numero > 0:
            extenso += unidades[numero]

    return extenso

numero = int(input('Digite um número entre 1 e 1000: '))

if numero >= 1 and numero <= 1000:
    extenso = numero_extenso(numero)
    print(extenso)
else:
    print('Número inválido. Digite um número entre 1 e 1000.')
