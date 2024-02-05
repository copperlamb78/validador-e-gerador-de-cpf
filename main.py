import random
import os
import json

cpfs = []

def limpar():
    os.system('clear')

def valida_primeiro_digito(cpf):
    
    lista = list(map(int, cpf[:9]))
    multiplicador = 1
    resultado = 0

    for numeros in lista:
       resultado = resultado + (numeros * multiplicador)
       multiplicador += 1

    resultado = resultado % 11

    if resultado == 10:
       resultado = 0
    return resultado

def valida_segundo_digito(cpf, digito_1):
    
    lista = list(map(int, cpf[:9] + str(digito_1)))
    multiplicador = 0
    resultado = 0

    for numeros in lista:
        resultado = resultado + (numeros * multiplicador)
        multiplicador += 1
    resultado = resultado % 11

    if resultado == 10:
        resultado = 0
    return resultado

def valida_cpf_completo(cpf, digito_1, digito_2):

    if cpf == str(cpf[:9]) + str(digito_1) + str(digito_2):
        print('CPF Verdadeiro')
        return
    
    else:
        print('CPF Falso!')
        return

def gera_cpf(qnt):
    global cpfs
    for _ in range(int(qnt)):
        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))
        
        digito_1 = valida_primeiro_digito(nove_digitos)
        digito_2 = valida_segundo_digito(nove_digitos, digito_1)
        print(f'{nove_digitos}-{digito_1}{digito_2}')
        cpf = nove_digitos + str(digito_1) + str(digito_2)
        cpfs += [cpf]


while True:
    print('Gerar CPF -------- [1]')
    print('Validar CPF ------ [2]')
    print('Sair ------------- [3]')
    entrada = input('O que deseja fazer? ')
    limpar()

    if not entrada.isdigit():
        limpar()
        print('ERRO!! Digite um número para as opções.')
        continue

    if len(entrada) != 1 or entrada not in '123':
        limpar()
        print('ERRO!! Digite uma opção válida.')

    if entrada == '1':
        while True:
            
            entrada = input('Quantos CPFs deseja gerar? 1-100: ')

            if not entrada.isdigit():
                limpar()
                print('ERRO!! Digite a quantidade em números.')
                continue

            if int(entrada) > 100 or int(entrada) < 1:
                limpar()
                print('ERRO!! Digite uma quantidade válida.')
                continue

            print('')
            gera_cpf(entrada)
            print('')
            break

    elif entrada == '2':
        
        while True:
            
            entrada = input('Digite o CPF para verificarmos: ')
        
            if not entrada.isdigit():
                limpar()
                print('ERRO!! Você digitou letras.')
                continue

            if len(entrada) != 11:
                limpar()
                print('ERRO!! Este CPF está faltando digitos.')
                continue

            limpar()
            digito_1 = valida_primeiro_digito(entrada)
            digito_2 = valida_segundo_digito(entrada, digito_1)
            valida_cpf_completo(entrada, digito_1, digito_2)
            print()
            break

    elif entrada == '3':
        if len(cpfs) > 0:
            
            while True: 
                entrada = input('Deseja salvar os CPFs gerados? [S]im/[N]ão: ').lower()
                if entrada.isdigit() or len(entrada) > 1:
                    limpar()
                    print('ERRO!! digite apenas [S] ou [N].')
                    continue

                if entrada not in 'sn':
                    limpar()
                    print('ERRO!! Opção desconhecida.')
                    continue

                if entrada == 's':
                    with open('cpfs_gerados.json', 'w') as arquivo:
                        json.dump(
                            cpfs,
                            arquivo,
                            indent=2
                        )

                break

        print('Finalizando Sistema...')
        break