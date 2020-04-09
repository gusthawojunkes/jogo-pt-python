import sys
import string
import os

def questao_1 ():
        os.system('cls')
        print()
        print(' ------------------------Questão 01------------------------')
        print(' Com o gado ficando mais magro e morrendo mais a cada dia, ')
        print(' os donos da fazenda e chefes de José Silva o pressionam ')
        print(' para que ele consiga tirar lucro da situação. O que José')
        print(' deverá fazer?')
        print(' ----------------------------------------------------------')
        print()
        print()
        print(' 1) José começa a despedir seus empregados, na esperança de')
        print('    cortar gastos e esperar a seca passar, mantendo o gado ')
        print('    restante.')
        print()
        print(' 2) José vai à cidade grande em busca de alguém interessado')
        print('    em comprar o gado, mesmo tendo todas as vacas magras e ')
        print('    doentes.')
        print()
        print(' 3) José libera uma parte do gado, para poder focar os ')
        print('    recursos em um grupo menor de vacas.')
        print()
        print()
        opq1 = input(' Qual a sua escolha? ')
        if opq1 == '1':
                os.system('cls')
                print()
                print(' ----------------------------------------------------------')
                print(' Mesmo com menos empregados, o dinheiro que sobra não é o')
                print(' bastante para manter o gado vivo até o fim da seca. As ')
                print(' vacas vão lentamente morrendo. Após um tempo, José fica ')
                print(' sem gado, e consequentemente, sem emprego.')
                print(' ----------------------------------------------------------')
                prox = input(' Ir para a próxima questão? [S/N] ')
                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                        questao_2()
                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                        menu()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_2()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
        elif opq1 == '2':
                os.system('cls')
                print()
                print(' ----------------------------------------------------------')
                print(' Na cidade, José consegue encontrar um professor de ')
                print(' faculdade, que está disposto a comprar todo o gado de José,')
                print(' mesmo que por um preço muito baixo. Sem mais ter gado para')
                print(' cuidar, os donos da fazendo despedem a todos, incluso José.')
                print(' ----------------------------------------------------------')
                prox = input(' Ir para a próxima questão? [S/N] ')
                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                        questao_2()
                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                        menu()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_2()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
        elif opq1 == '3':
                os.system('cls')
                print()
                print(' ----------------------------------------------------------')
                print(' Mesmo com menos gado para cuidar, e mais recursos centrados')
                print(' em menos vacas, a doença que circula entre as vacas é mais')
                print(' forte que os remédios disponíveis. O gado vai morrendo com')
                print(' com o tempo. Sem gado para cuidar, José é despedido.')
                print(' ----------------------------------------------------------')
                prox = input(' Ir para a próxima questão? [S/N] ')
                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                        questao_2()
                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                        menu()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_2()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
        else:
                print()
                print(' Selecione apenas números de 1 a 3.')
                while True:
                        opq1 = input(' Qual a sua escolha? ')
                        if opq1 == '1':
                                os.system('cls')
                                print()
                                print(' ----------------------------------------------------------')
                                print(' Mesmo com menos empregados, o dinheiro que sobra não é o')
                                print(' bastante para manter o gado vivo até o fim da seca. As ')
                                print(' vacas vão lentamente morrendo. Após um tempo, José fica ')
                                print(' sem gado, e consequentemente, sem emprego.')
                                print(' ----------------------------------------------------------')
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_2()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                prox = input(' Ir para a próxima questão? [S/N] ')
                                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                                        questao_2()
                                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                                        menu()
                        elif opq1 == '2':
                                os.system('cls')
                                print()
                                print(' ----------------------------------------------------------')
                                print(' Na cidade, José consegue encontrar um professor de ')
                                print(' faculdade, que está disposto a comprar todo o gado de José,')
                                print(' mesmo que por um preço muito baixo. Sem mais ter gado para')
                                print(' cuidar, os donos da fazendo despede a todos, incluso José.')
                                print(' ----------------------------------------------------------')
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_2()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                prox = input(' Ir para a próxima questão? [S/N] ')
                                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                                        questao_2()
                                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                                        menu()
                        elif opq1 == '3':
                                os.system('cls')
                                print()
                                print(' ----------------------------------------------------------')
                                print(' Mesmo com menos gado para cuidar, e mais recursos centrados')
                                print(' em menos vacas, a doença que circula entre as vacas é mais')
                                print(' forte que os remédios disponíveis. O gado vai morrendo com')
                                print(' com o tempo. Sem gado para cuidar, José é despedido.')
                                print(' ----------------------------------------------------------')
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_2()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                prox = input(' Ir para a próxima questão? [S/N] ')
                                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                                        questao_2()
                                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                                        menu()


def questao_2():
        os.system('cls')
        print()
        print(' ------------------------Questão 02------------------------')
        print(' Sem emprego, e com o dinheiro acabando José se vê em uma') 
        print(' situação complicada, pois é o único sustento de uma ')
        print(' família de 6 (ele mesmo, sua esposa, sua filha mais velha,')
        print(' dois outros filhos e uma criança ainda de colo). Ele se vê')
        print(' na escolha mais importante de sua vida. O que José deverá')
        print(' fazer?')
        print(' ----------------------------------------------------------')
        print()
        print()
        print(' 1) José procura por qualquer emprego no vilarejo, mesmo ')
        print('    sabendo que ninguém na vila tinha condições de ')
        print('    contratar alguém.')
        print()
        print(' 2) José ouviu falar de uma favela que o governo sustentava')
        print('    no meio do sertão e decide levar a sua família para lá,')
        print('    mesmo sabendo que as situações lá são precárias.')
        print()
        print(' 3) José sabe que estão começando a descobrir a Mata no')
        print('    Amazonas, e com certeza ele conseguirá emprego lá, ')
        print('    porém, não é uma viagem pequena, ainda mais para as')
        print('    crianças, José tem medo que ela não aguentem  uma ')
        print('    viagem tão longa.')
        print()
        print()
        opq2 = input(' Qual a sua escolha? ')
        if opq2 == '1':
                os.system('cls')
                print()
                print(' ------------------------VOCÊ PERDEU-----------------------')
                print(' Por mais  que ele procure, ele não acha nada no vilarejo,')
                print(' com isso, ele entra em uma grande depressão, que por não ')
                print(' ser tratada, causa o suicídio de José.')
                print(' ----------------------------------------------------------')
                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                        menu()
                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                        sys.exit()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()

        elif opq2 == '2':
                os.system('cls')
                print()
                print(' ------------------------VOCÊ PERDEU-----------------------')
                print(' Ele e sua família se mudam para a favela, porém, sem ter o')
                print(' menor saneamento básico, uma  doença se alastrou por todas')
                print(' os habitantes do local, e sua família também. Todos morrem')
                print(' de Varíola.')
                print(' ----------------------------------------------------------')
                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                        menu()
                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                        sys.exit()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
        elif opq2 == '3':
                os.system('cls')
                print()
                print(' ----------------------------------------------------------')
                print(' Mesmo sabendo que terão uma viagem difícil, José e sua')
                print(' família juntam as coisas, e partem em busca de uma vida ')
                print(' melhor em outro estado.')
                print(' ----------------------------------------------------------')
                prox = input(' Ir para a próxima questão? [S/N] ')
                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                        questao_3()
                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                        menu()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_3()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()

        else:
                print()
                print('Selecione apenas números de 1 a 3.')
                while True:
                        opq2 = input(' Qual a sua escolha? ')
                        if opq2 == '1':
                                os.system('cls')
                                print()
                                print(' ------------------------VOCÊ PERDEU-----------------------')
                                print(' Por mais  que ele procure, ele não acha nada no vilarejo,')
                                print(' com isso, ele entra em uma grande depressão, que por não ')
                                print(' ser tratada, causa o suicídio de José.')
                                print(' ----------------------------------------------------------')
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                                        sys.exit()

                        elif opq2 == '2':
                                os.system('cls')
                                print()
                                print(' ------------------------VOCÊ PERDEU-----------------------')
                                print(' Ele e sua família se mudam para a favela, porém, sem ter o')
                                print(' menor saneamento básico, uma  doença se alastrou por todas')
                                print(' os habitantes do local, e sua família também. Todos morrem')
                                print(' de Varíola.')
                                print(' ----------------------------------------------------------')
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                                        sys.exit()
                        elif opq2 == '3':
                                os.system('cls')
                                print()
                                print(' ----------------------------------------------------------')
                                print(' Mesmo com menos gado para cuidar, e mais recursos centrados')
                                print(' em menos vacas, a doença que circula entre as vacas é mais')
                                print(' forte que os remédios disponíveis. O gado vai morrendo com')
                                print(' o tempo. Sem gado para cuidar, José é despedido.')
                                print(' ----------------------------------------------------------')
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_3()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                prox = input(' Ir para a próxima questão? [S/N] ')
                                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                                        questao_3()
                                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                                        menu()

                
                                
def questao_3():
        os.system('cls')
        print()
        print(' ------------------------Questão 03------------------------')
        print(' A única maneira de passar pelo agreste é caminhando e para')
        print(' carregar os suprimento de sua família, ele compra um burro,')
        print(' que no meio do caminho adoece. O que José deverá fazer?')
        print(' ----------------------------------------------------------')
        print()
        print()
        print(' 1) Acabar com o sofrimento do burro logo agora, abandonar')
        print('    as coisas desnecessárias e levar consigo somente ')
        print('    suprimentos como comida e água.')
        print()
        print(' 2) Gastar o resto de seu dinheiro em remédios para o burro')
        print('    na esperança que ele melhore.')
        print()
        print(' 3) Deixar que o burro morra naturalmente e usar  a sua')
        print('    carne como alimento.')
        print()
        print()
        opq3 = input(' Qual a sua escolha? ')
        if opq3 == '1':
                os.system('cls')
                print()
                print(' ----------------------------------------------------------')
                print(' Matar o burro agora parece a coisa mais humana a se fazer,')
                print(' e mesmo que deixar seus bens para trás, o promessa de uma ')
                print(' vida nova ainda é a única esperança.')
                print(' ----------------------------------------------------------')
                prox = input(' Ir para a próxima questão? [S/N] ')
                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                        questao_4()
                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                        menu()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_4()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
        elif opq3 == '2':
                os.system('cls')
                print()
                print(' ------------------------VOCÊ PERDEU-----------------------')
                print(' O vendedor ambulante que lhe vende o remédio não parecia ')
                print(' muito confiável, e não era. Invés de lhe vender remédio, ')
                print(' ele simplesmente lhe vendeu água. Com  a morte do burro e ')
                print(' sem dinheiro, José sabe que condenou a sua família à morte.')
                print(' ----------------------------------------------------------')
                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                        menu()
                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                        sys.exit()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()

        elif opq3 == '3':
                os.system('cls')
                print()
                print(' ------------------------VOCÊ PERDEU-----------------------')
                print(' Quando o burro finalmente morre, José e sua esposa ')
                print(' aproveitam a carne do animal. Mas, infelizmente, só assar ')
                print(' a carne do animal não foi o suficiente, e ao consumi-la, ')
                print(' todos da família ficam doentes, e lentamente, um a um, ')
                print(' desistem da vida.')
                print(' ----------------------------------------------------------')
                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                        menu()
                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                        sys.exit()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()

        else:
                print()
                print(' Selecione apenas números de 1 a 3.')
                while True:
                        opq3 = input(' Qual a sua escolha? ')
                        if opq3 == '1':
                                os.system('cls')
                                print()
                                print(' ----------------------------------------------------------')
                                print(' Matar o burro agora parece a coisa mais humana a se fazer,')
                                print(' e mesmo que deixar seus bens para trás, o promessa de uma ')
                                print(' vida nova ainda é a única esperança.')
                                print(' ----------------------------------------------------------')
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_4()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                prox = input(' Ir para a próxima questão? [S/N] ')
                                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                                        questao_4()
                                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                                        menu()
                        elif opq3 == '2':
                                os.system('cls')
                                print()
                                print(' ------------------------VOCÊ PERDEU-----------------------')
                                print(' O vendedor ambulante que lhe vende o remédio não parecia ')
                                print(' muito confiável, e não era. Invés de lhe vender remédio, ')
                                print(' ele simplesmente lhe vendeu água. Com  a morte do burro e ')
                                print(' sem dinheiro, José sabe que condenou a sua família à morte.')
                                print(' ----------------------------------------------------------')
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                                        sys.exit()

                        elif opq3 == '3':
                                os.system('cls')
                                print()
                                print(' ------------------------VOCÊ PERDEU-----------------------')
                                print(' Quando o burro finalmente morre, José e sua esposa ')
                                print(' aproveitam a carne do animal. Mas, infelizmente, só assar ')
                                print(' a carne do animal não foi o suficiente, e ao consumi-la, ')
                                print(' todos da família ficam doentes, e lentamente, um a um, ')
                                print(' desistem da vida.')
                                print(' ----------------------------------------------------------')
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                                        sys.exit()



def questao_4():
        os.system('cls')
        print()
        print(' ------------------------Questão 04------------------------')
        print(' José sempre soube que a viagem não seria fácil, e que ')
        print(' passariam muitas dificuldades, mas as crianças não ')
        print(' entendiam isso direito, e o tempo todo, choravam de fome.')
        print(' O que José deverá fazer?')
        print(' ----------------------------------------------------------')
        print()
        print()
        print(' 1) Negar comida para as crianças, pois sabe que ela será')
        print('    necessária depois.')
        print()
        print(' 2) Ir até a cidade mais próxima e ver se uma boa família')
        print('    quer adotar uma das crianças.')
        print()
        print(' 3) Dar a sua parte para saciar a fome das crianças, ')
        print('    mesmo que isso signifique passar fome nos próximos dias.')
        print()
        print()
        opq4 = input(' Qual a sua escolha? ')
        if opq4 == '1':
                os.system('cls')
                print()
                print(' ----------------------------------------------------------')
                print(' Com fome, um dos garotos de distância da família e acha ')
                print(' um aipim, e come, sem antes preparar de forma correta, é')
                print(' venenoso para o consumo, o que infelizmente o garoto ')
                print(' não sabe, e morre. Por mais triste que seja, ainda é ')
                print(' uma boca a menos para alimentar.')
                print(' ----------------------------------------------------------')
                prox = input(' Ir para a próxima questão? [S/N] ')
                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                        questao_5()
                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                        menu()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_5()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
        elif opq4 == '2':
                os.system('cls')
                print()
                print(' ------------------------VOCÊ PERDEU-----------------------')
                print(' A mulher de José concorda que seria uma vida melhor para')
                print(' as duas crianças, e ele as deixa no orfanato da cidade mais')
                print(' próxima. Mesmo sabendo que os dois estão melhores assim, a')
                print(' mulher de José entra em depressão, o que é a ruína para o')
                print(' resto da família, que simplesmente preferem a morte do que')
                print(' este inferno em que vivem.')
                print(' ----------------------------------------------------------')
                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                        menu()
                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                        sys.exit()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
        elif opq4 == '3':
                os.system('cls')
                print()
                print(' ------------------------VOCÊ PERDEU-----------------------')
                print(' Ao que aparenta, dar a sua comida para as crianças as')
                print(' deixou mais calmas, porém, o que você não pensou foi que ')
                print(' a falta de comida lhe cobraria um preço muito alto, e você')
                print(' morre de fome.')
                print(' ----------------------------------------------------------')
                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                        menu()
                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                        sys.exit()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
        else:
                print()
                print(' Selecione apenas números de 1 a 3.')
                while True:
                        opq4 = input(' Qual a sua escolha? ')
                        if opq4 == '1':
                                os.system('cls')
                                print()
                                print(' ----------------------------------------------------------')
                                print(' Com fome, um dos garotos de distância da família e acha ')
                                print(' um aipim, e come, sem antes preparar de forma correta, é')
                                print(' venenoso para o consumo, o que infelizmente o garoto ')
                                print(' não sabe, e morre. Por mais triste que seja, ainda é ')
                                print(' uma boca a menos para alimentar.')
                                print(' ----------------------------------------------------------')
                                prox = input(' Ir para a próxima questão? [S/N] ')
                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                        questao_5()
                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                        menu()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                prox = input(' Ir para a próxima questão? [S/N] ')
                                                if prox == 'Sim' or prox == 'sim' or prox == 's' or prox == 'S' or prox == 'SIM': 
                                                        questao_5()
                                                elif prox == 'Não' or prox == 'não' or prox == 'n' or prox == 'N' or prox == 'NÃO' or prox == 'nao':
                                                        menu()
                        elif opq4 == '2':
                                os.system('cls')
                                print()
                                print(' ------------------------VOCÊ PERDEU-----------------------')
                                print(' A mulher de José concorda que seria uma vida melhor para')
                                print(' as duas crianças, e ele as deixa no orfanato da cidade mais')
                                print(' próxima. Mesmo sabendo que os dois estão melhores assim, a')
                                print(' mulher de José entra em depressão, o que é a ruína para o')
                                print(' resto da família, que simplesmente preferem a morte do que')
                                print(' este inferno em que vivem.')
                                print(' ----------------------------------------------------------')
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao' or voltar == 'NAO':
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao' or voltar == 'NAO':
                                                        sys.exit()
                        elif opq4 == '3':
                                os.system('cls')
                                print()
                                print(' ------------------------VOCÊ PERDEU-----------------------')
                                print(' Ao que aparenta, dar a sua comida para as crianças as')
                                print(' deixou mais calmas, porém, o que você não pensou foi que ')
                                print(' a falta de comida lhe cobraria um preço muito alto, e você')
                                print(' morre de fome.')
                                print(' ----------------------------------------------------------')
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                                        sys.exit()


def questao_5():
        os.system('cls')
        print()
        print(' ------------------------Questão 05------------------------')
        print(' Com um membro da família a menos, vocês persistem sonhando')
        print(' na nova vida, porém, seu dinheiro e comida já estão no')
        print(' final. Sabendo que há uma cidadela perto, você decide ir ')
        print(' até ela atrás de ajuda.')
        print(' O que José deverá fazer?')
        print(' ----------------------------------------------------------')
        print()
        print()
        print(' 1) No meio do caminho, você avista uma cabra dentro de uma')
        print('    fazendinha, sem ninguém vigiando, uma oportunidade')
        print('    perfeita para um pequeno roubo por necessidade.')
        print()
        print(' 2) Você decide procurar por um trabalho no cidadela, mesmo')
        print('    sabendo que seria muito difícil alguém dar emprego a um')
        print('    forasteiro, ainda mais no meio da seca.')
        print()
        print(' 3) Você decide mendigar por dinheiro e comida na cidade, ')
        print('    por mais humilhante que seja esta ideia, na sua')
        print('    situação, não há ideias ruins.')
        print()
        print()
        opq5 = input(' Qual a sua escolha? ')
        if opq5 == '1':
                os.system('cls')
                print()
                print(' ------------------------VOCÊ PERDEU-----------------------')
                print(' Bem, acontece que não era a oportunidade perfeita para um ')
                print(' assalto, e tinha sim alguém vendo a cabra, o dono. Sem')
                print(' aviso prévio, ele atira contra você, e seu peito ')
                print(' ensanguentado é a sua última visão.')
                print(' ----------------------------------------------------------')
                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                        menu()
                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                        sys.exit()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM' :
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
        elif opq5 == '2':
                os.system('cls')
                print()
                print(' ------------------------VOCÊ GANHOU-----------------------')
                print(' Por mais incrível que pareça, José consegue um emprego na')
                print(' cidadela. De pouquinho em pouquinho, você e sua família')
                print(' constroem uma nova vida.')
                print(' ----------------------------------------------------------')
                print()
                print()
                print(' Parabéns! Você finalizou o jogo e fez todas as escolhas ')
                print(' certas para se manter vivo.')
                print()
                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                        menu()
                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                        sys.exit()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()


        elif opq5 == '3':
                os.system('cls')
                print()
                print(' ------------------------VOCÊ GANHOU-----------------------')
                print(' Ao bater na porta de uma casa, José dá de cara com um Tio,')
                print(' que era cornel na cidade. Comovido com a sua história, ele')
                print(' ajuda sua família, e comprar passagens de trem para todos ')
                print(' até a capital do Amazonas. José e sua família, chegam no ')
                print(' destino final, e começam uma nova vida.')
                print(' ----------------------------------------------------------')
                print()
                print()
                print(' Parabéns! Você finalizou o jogo e fez todas as escolhas ')
                print(' certas para se manter vivo.')
                print()
                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                        menu()
                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                        sys.exit()
                else:
                        print()
                        print(' Insira apenas "Sim" ou "Não".')
                        while True:
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
        else:
                print()
                print(' Selecione apenas números de 1 a 3.')
                while True:
                        opq5 = input(' Qual a sua escolha? ')
                        if opq5 == '1':
                                os.system('cls')
                                print()
                                print(' ------------------------VOCÊ PERDEU-----------------------')
                                print(' Bem, acontece que não era a oportunidade perfeita para um ')
                                print(' assalto, e tinha sim alguém vendo a cabra, o dono. Sem')
                                print(' aviso prévio, ele atira contra você, e seu peito ')
                                print(' ensanguentado é a sua última visão.')
                                print(' ----------------------------------------------------------')
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM' :
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                                        sys.exit()
                        elif opq5 == '2':
                                os.system('cls')
                                print()
                                print(' ------------------------VOCÊ GANHOU-----------------------')
                                print(' Por mais incrível que pareça, José consegue um emprego na')
                                print(' cidadela. De pouquinho em pouquinho, você e sua família')
                                print(' constroem uma nova vida.')
                                print(' ----------------------------------------------------------')
                                print()
                                print()
                                print(' Parabéns! Você finalizou o jogo e fez todas as escolhas ')
                                print(' certas para se manter vivo.')
                                print()
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                                        sys.exit()


                        elif opq5 == '3':
                                os.system('cls')
                                print()
                                print(' ------------------------VOCÊ GANHOU-----------------------')
                                print(' Ao bater na porta de uma casa, José dá de cara com um Tio,')
                                print(' que era cornel na cidade. Comovido com a sua história, ele')
                                print(' ajuda sua família, e comprar passagens de trem para todos ')
                                print(' até a capital do Amazonas. José e sua família, chegam no ')
                                print(' destino final, e começam uma nova vida.')
                                print(' ----------------------------------------------------------')
                                print()
                                print()
                                print(' Parabéns! Você finalizou o jogo e fez todas as escolhas ')
                                print(' certas para se manter vivo.')
                                print()
                                voltar = input(' Deseja voltar ao menu principal? [S/N] ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                                        sys.exit()




        

        
def menu():
    os.system('cls')
    print()
    print(' ----------------------------O QUINZE----------------------------')
    print()
    print(' Bem-vindo à adaptação do livro "O Quinze", de Rachel de Queiroz.')
    print()
    print(' ------------------------------Menu------------------------------')
    print()
    print(' 1 - Jogar')
    print(' 2 - Instruções')
    print(' 3 - Um breve resumo')
    print()
    opc = input(' Escolha a opção desejada: ')
    
    if opc == '3':
        os.system('cls')        
        print()
        print(' José Silva, é um homem de família, trabalha em uma fazendo cuidando dos bois, manda em seus empregados e ')
        print(' tem uma posição de respeito no vilarejo em que vive. Por causa da seca severa que aflige o Nordeste, o gado ')
        print(' que está sob seus cuidados começa a morrer de fome e doença, e o seu estilo de vida está ameaçado.')
        print()
        voltar = input(' Retornar ao menu? [S/N]: ')
        if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                os.system('cls')
                menu()
        elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                print()
                print('Aplicação finalizada.')
                os.system('cls')
                sys.exit()
        else:
                print()
                print(' Insira apenas "Sim" ou "Não".')
                while True:
                        voltar = input(' Retornar ao menu? [S/N]: ')
                        if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                os.system('cls')
                                menu()
                        elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                print()
                                print('Aplicação finalizada.')
                                os.system('cls')
                                sys.exit()
                        
                        
    elif opc == '2':
        os.system('cls')
        print()
        print(' O Jogo tem o intuito de fazer com que o jogador conheça a obra "O Quinze" de Rachel de Queiroz')
        print()
        print(' Como Jogar?')
        print()
        print(' É muito simples, o jogo consiste em escolhas, que fazem seu personagem sobreviver à seca ou não.')
        print(' Se você conhecer a obra, será fácil de ganhar, caso não conheça, essa é a hora de aprender!')
        print()
        voltar = input(' Retornar ao menu? [S/N]: ')
        if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                os.system('cls')
                menu()
        elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                print()
                print('Aplicação finalizada.')
                os.system('cls')
                sys.exit()
        else:
                print()
                print(' Insira apenas "Sim" ou "Não".')
                while True:
                        voltar = input(' Retornar ao menu? [S/N]: ')
                        if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                os.system('cls')
                                menu()
                        elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                print()
                                print('Aplicação finalizada.')
                                os.system('cls')
                                sys.exit()



    elif opc == '1':
        os.system('cls')
        print()
        abacaxi = input(' Pronto para começar? [S/N] ')
        if abacaxi == 'Não' or abacaxi == 'não' or abacaxi == 'n' or abacaxi == 'N' or abacaxi == 'NÂO' or abacaxi == 'nao':
                os.system('cls')
                menu()

        elif abacaxi == 'Sim' or abacaxi == 'sim' or abacaxi == 's' or abacaxi == 'S' or abacaxi == 'SIM': 
                questao_1()
                
        else:
                print()
                print(' Insira apenas "Sim" ou "Não".')
                while True:
                        abacaxi = input(' Pronto para começar? [S/N] ')
                        if abacaxi == 'Não' or abacaxi == 'não' or abacaxi == 'n' or abacaxi == 'N' or abacaxi == 'NÂO' or abacaxi == 'nao':
                                os.system('cls')
                                menu()

                        elif abacaxi == 'Sim' or abacaxi == 'sim' or abacaxi == 's' or abacaxi == 'S' or abacaxi == 'SIM': 
                                questao_1()    

    else:
                print()
                print(' Insira apenas números de 1 a 3.')
                
                while True:
                        opc = input(' Escolha a opção desejada: ')
                        if opc == '3':
                                os.system('cls')        
                                print()
                                print(' José Silva, é um homem de família, trabalha em uma fazendo cuidando dos bois, manda em seus empregados e ')
                                print(' tem uma posição de respeito no vilarejo em que vive. Por causa da seca severa que aflige o Nordeste, ')
                                print(' o gado que está sob seus cuidados começa a morrer de fome e doença, e o seu estilo de vida está ameaçado.')
                                print()
                                voltar = input(' Retornar ao menu? [S/N]: ')
                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                        os.system('cls')
                                        menu()
                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                        print()
                                        print('Aplicação finalizada.')
                                        os.system('cls')
                                        sys.exit()
                                else:
                                        print()
                                        print(' Insira apenas "Sim" ou "Não".')
                                        while True:
                                                voltar = input(' Retornar ao menu? [S/N]: ')
                                                if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                                        os.system('cls')
                                                        menu()
                                                elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao':
                                                        print()
                                                        print('Aplicação finalizada.')
                                                        os.system('cls')
                                                        sys.exit()
                                
                                
                        elif opc == '2':
                                os.system('cls')
                                print()
                                print(' O Jogo tem o intuito de fazer com que o jogador conheça a obra "O Quinze" de Rachel de Queiroz')
                                print()
                                print(' Como Jogar?')
                                print()
                                print(' É muito simples, o jogo consiste em escolhas, que fazem seu personagem sobreviver à seca ou não')
                                print(' Se você conhecer a obra, será fácil de ganhar, caso não conheça, essa é a hora de aprender!')


                        elif opc == '1':
                                os.system('cls')
                                print()
                                abacaxi = input(' Pronto para começar? [S/N] ')
                                if abacaxi == 'Não' or abacaxi == 'não' or abacaxi == 'n' or abacaxi == 'N' or abacaxi == 'NÂO' or abacaxi == 'nao':
                                        os.system('cls')
                                        menu()

                                elif abacaxi == 'Sim' or abacaxi == 'sim' or abacaxi == 's' or abacaxi == 'S' or abacaxi == 'SIM': 
                                        questao_1()

def voltar():
        voltar = input(' Deseja voltar ao menu principal? [S/N] ')
        if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                menu()
        elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao' or voltar == 'NAO':
                sys.exit()
        else:
                print()
                print(' Insira apenas "Sim" ou "Não".')
                while True:
                        if voltar == 'Sim' or voltar == 'sim' or voltar == 's' or voltar == 'S' or voltar == 'SIM':
                                menu()
                        elif voltar == 'Não' or voltar == 'não' or voltar == 'n' or voltar == 'N' or voltar == 'NÂO' or voltar == 'nao' or voltar == 'NAO':
                                print(' Aplicação finalizada.')
                                sys.exit()
menu()