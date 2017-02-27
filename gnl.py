'''
@autor: Prince
@date: 13/02/2017
Scanner de portas criado para rodar em python e no sistema operacional windows
'''


import argparse, random as aleatorio, datetime, os
dic = {}
concurso =''
data=''
concursoData=''
lista3=''
def converterListaStringOrdenar(lista):
    '''
    :param lista:recebe uma lista com dados em string e converte para numeros inteiros
    :return
    '''
    lista = lista
    a = str(lista).replace('[', '')
    a = a.replace(']', '')
    lista = []
    for x in a.replace('\'', '').split(','):
        lista.append(int(x))
        lista.sort()
    return lista
def geradorSorteio(semente='', numeroMinimo=1, numeroMaximo=60, gerarNumeros=6):
    ''''
    :param semente:Se a semente receber valor 'vazio', o procedimento ira gerar numeros aleatorios com base na data do computador
    :return: Uma lista ordenada de forma crescente com os numeros sorteados
    ->Criar uma lista e um dicionario local sem informaçoes iniciais
    ->Verificar o conteudo da semente, se vazia determinar a semente como data do O.S, se não aplicar a semente ao conteudo informado pelo usuário
    ->Determinar o range de numeros possiveis a serem sorteados com base nas informações determinadas pelo usuário
    ->Criar um laço de repetição para realizar o sorteio de numeros em 'X' vezes determinado pelo usuário
    ->Armazenar o numero em um dicionario de dados a fim de evitar a duplicata de informações/numeros sorteados
    ->Passar os dados sorteados para uma lista, ordenar e retornar a informação
    '''
    if semente == '':
        aleatorio.seed(datetime.datetime.now())
        msg1 = 'Semente definida pela data do PC %s' % str(datetime.datetime.now())  # <---linha de Comentario
    elif semente != '':
        aleatorio.seed(str(semente))
        msg1 = 'Semente defininda pelo usuario %s' % str(aleatorio.random())  # <---linha de Comentario
    var_lista_apoio = []
    var_dicionario = set()
    for x in range(numeroMinimo, numeroMaximo + 1): # definindo o range
        if var_dicionario.__len__() < gerarNumeros: # definindo a quantidade de sorteios
            var_dicionario.add(aleatorio.randrange(numeroMinimo, numeroMaximo)) # adcionando ao dicionario o numero sorteado sem duplicatas
    for x in var_dicionario: # fazendo a leitura dos dados do dicionario
        var_lista_apoio.append(x) #passando o valor dos dados do dicionairo para uma lista
        var_lista_apoio.sort() #ordenando a lista
    return var_lista_apoio #retornando a lista
def imprimirResultadoDicionario(dicionario):
    '''
    Realiza a impressão do dicionario
    :param dicionario: recebe o dicionario a ser impresso
    :return: n/a
    '''
    for x in sorted(dicionario):
        print(x, '=', dicionario[x])
def verificaAcerto(lista_arquivo, lista, acertoMinimo = 4):
    lista_apoio = []
    for x in lista:
        for y in lista_arquivo:
            if x == y:
                lista_apoio.append(x)
    if lista_apoio.__len__() >= acertoMinimo:
        retornar = str(lista_apoio.__len__())+' Parabéns '
    else:
        retornar = str(lista_apoio.__len__())+'          '
    return retornar
def lerArquivo(arquivo, semente='', numeroMinimo=1, numeroMaximo=60, gerarNumeros=6, acertoMinimo=4):
    '''
    Este arquivo a ser aberto, deve ser mantido e atualizado manualmente pelo usuario
    cada linha contem
    1737,17022017,61,40,72,83,7,38,68,37,74,67,59,65,77,85,60,63,71,93,51,33
    concurso,data,numeros sorteados
    OBS: os numeros devem seguir padrão de numeros inteiros ex: se o numero for 7 não inserir 07

    :param arquivo: Nome do arquivo de texto para leitura conversão para Concurso, Data, ConcursoData, Lista(dos numeros sorteados)
    :return:
    '''
    arquivo_leitura = str(arquivo) + '.txt'
    nm = numeroMinimo
    nma = numeroMaximo
    gn = gerarNumeros
    acm = acertoMinimo
    dados = open(arquivo_leitura) #Abrindo o arquivo de texto com as informações do Concurso com Data e os numeros sorteados
    if arquivo == 'lotofacil':
        var_final = 17
    if arquivo == 'lotomania':
        var_final = 22
    if arquivo == 'megasena':
        var_final = 8
    if arquivo == 'quina':
        var_final = 7
    if arquivo == 'timemania':
        var_final = 9
    if arquivo == 'duplasena':
        for x in dados:  # Processo a ser realizado para cada linha lida no arquivo
            lista2 = []  # definida uma lista sem dados
            lista3 = []  #definindo uma lista sem dados
            lista1 = x.split(',')  # registrando o conteudo da linha em uma string separando os dados por uma virgula

            for x in range(2,8):  # Processo a ser realizado em cada item separado por virgula, neste caso apartir do item 2 ate o item 8
                lista2.append(lista1[x])  # Adcionando em uma lista os itens separados por virgula do item 2 ate o 22, o dado 0 e 1 são referentes a data e concurso

            a = str(lista2).replace('[', '')
            a = a.replace(']', '')
            lista2f = []
            for x in a.replace('\'', '').split(','):
                lista2f.append(int(x))
                lista2f.sort()

            for x in range(9,15):
                lista3.append(lista1[x])
            a = str(lista3).replace('[', '')
            a = a.replace(']', '')
            lista3f = []
            for x in a.replace('\'', '').split(','):
                lista3f.append(int(x))
                lista3f.sort()

            concurso = lista1[0]  # pegando o concurso do sorteio registrado na string 'lista'
            data = lista1[1]  # pegando a data do concurso do sorteio registrado na string 'lista'


            lista_arquivo2 = converterListaStringOrdenar(lista2f)  # convertendo a lista2 que e composta em string para int
            lista_arquivo3 = converterListaStringOrdenar(lista3f)
            # Gerando listas com as sementes
            ger_concurso = geradorSorteio(semente=concurso, numeroMinimo=nm, numeroMaximo=nma, gerarNumeros=gn)
            ger_data = geradorSorteio(semente=data, numeroMinimo=nm, numeroMaximo=nma, gerarNumeros=gn)
            ger_concurso_data = geradorSorteio(semente=concurso + data, numeroMinimo=nm, numeroMaximo=nma, gerarNumeros=gn)
            ger_outra_semente = geradorSorteio(semente=semente, numeroMinimo=nm, numeroMaximo=nma, gerarNumeros=gn)

            print('Data', data, 'Concurso', concurso, lista_arquivo2, lista_arquivo3)
            print('J1 Semente   :Acerto', verificaAcerto(lista_arquivo2, ger_outra_semente, acertoMinimo=acm),ger_outra_semente)
            print('J2 Semente   :Acerto', verificaAcerto(lista_arquivo3, ger_outra_semente, acertoMinimo=acm),ger_outra_semente)
            print('J1 SementeC  :Acerto', verificaAcerto(lista_arquivo2, ger_concurso, acertoMinimo=acm),ger_concurso)
            print('J2 SementeC  :Acerto', verificaAcerto(lista_arquivo3, ger_concurso, acertoMinimo=acm),ger_concurso)
            print('J1 SementeD  :Acerto', verificaAcerto(lista_arquivo2, ger_data, acertoMinimo=acm), ger_data)
            print('J2 SementeD  :Acerto', verificaAcerto(lista_arquivo3, ger_data, acertoMinimo=acm), ger_data)
            print('J1 SementeCD :Acerto', verificaAcerto(lista_arquivo2, ger_concurso_data, acertoMinimo=acm), ger_concurso_data)
            print('J2 SementeCD :Acerto', verificaAcerto(lista_arquivo3, ger_concurso_data, acertoMinimo=acm), ger_concurso_data)



            print('\n\n')

    for x in dados: #Processo a ser realizado para cada linha lida no arquivo
        lista2 = [] #definida uma lista sem dados
        lista = x.split(',') #registrando o conteudo da linha em uma string separando os dados por uma virgula

        for y in range(2, var_final): #Processo a ser realizado em cada item separado por virgula, neste caso apartir do item 2 ate o item 22
            lista2.append(lista[y]) #Adcionando em uma lista os itens separados por virgula do item 2 ate o 22, o dado 0 e 1 são referentes a data e concurso

        concurso = lista[0]  # pegando o concurso do sorteio registrado na string 'lista'
        data = lista[1]  # pegando a data do concurso do sorteio registrado na string 'lista'
        lista_arquivo = converterListaStringOrdenar(lista2) #convertendo a lista2 que e composta em string para int

        #Gerando listas com as sementes
        ger_concurso = geradorSorteio(semente=concurso, numeroMinimo=nm, numeroMaximo=nma,gerarNumeros=gn)
        ger_data = geradorSorteio(semente=data, numeroMinimo=nm, numeroMaximo=nma,gerarNumeros=gn)
        ger_concurso_data = geradorSorteio(semente=concurso+data, numeroMinimo=nm, numeroMaximo=nma,gerarNumeros=gn)
        ger_outra_semente = geradorSorteio(semente=semente, numeroMinimo=nm, numeroMaximo=nma,gerarNumeros=gn)

        print('Data',data,'Concurso',concurso,lista_arquivo,lista_arquivo.__len__(),'\n'
        'Semente   :Acerto', verificaAcerto(lista_arquivo, ger_outra_semente, acertoMinimo=acm),'            Numeros Gerados',ger_outra_semente,'\n'
        'SementeC  :Acerto', verificaAcerto(lista_arquivo, ger_concurso, acertoMinimo=acm),'            Numeros Gerados',ger_concurso,'\n'
        'SementeD  :Acerto', verificaAcerto(lista_arquivo, ger_data, acertoMinimo=acm),'            Numeros Gerados',ger_data,'\n'
        'SementeCD :Acerto', verificaAcerto(lista_arquivo, ger_concurso_data, acertoMinimo=acm),'            Numeros Gerados',ger_concurso_data,'\n\n')

    dados.close() #Fechando o arquivo de texto
def gnl():
    '''
    :param: Não recebe paramentros
    :return: Não retorna dados(imprimir resultados na linha de comando)
    ->Software deve ser executado via linha de comando
    ->python 3.x
    ->Deve aceitar alterar o range de numeros sorteados uma vez que jogos como a mega-sena aceita numeros de 1 até 60 e lotomania aceita numeros de 0 até 99, visando alterações no range de numeros pela caixa
    ->O numero sorteado deverá ser igual toda vez que uma ancora/semente for usada, assim se o usuário usar uma palavra chave especifica sempre receberá o mesmo numeros sorteados
    ->A quantidade de sorteios deverá ser de 1 até 4 sorteios, sendo estes sorteios definidos pelo uso das sementes onde a ausencia de semente retornara 1 sorteio e todas as sementes defenidas retornará 4 sorteios
    ->deverá receber argumentos
    :arg semente opcional determina os numeros a serem sorteados
    :arg semetec opcional determina os numeros a serem sorteados
    :arg semented opcional determina os numeros a serem sorteados
    :arg sementecd opcional determina os numeros a serem sorteados
    :arg gerarnumeros opcional determina quantos numeros sortear
    :arg numerominimo opcional determina qual o numero inicial para sorteio, padrão será 0
    :arg numeromaximo opcional determina qual o numero maximo para o sorteio, padrâo sera 60
    :arg lista opcional recebe os numeros sorteados para analise dos resultados
    '''
    #descrição do software
    parser = argparse.ArgumentParser(description = '--- GNL --- Gerador de numeros lotericos, deselvolvido para facilitar a geração de numeros aleatorios ou numeros fixos  ----> Analista de Sistemas:PRINCE, Klayton Bueno')
    #recebendo parametros via linha de comando
    parser.add_argument('-s',dest='semente', action = 'store', default = '',required = False,help = 'Argumento opcional, se não for inserido valor neste argumento o software ira gerar numeros aleatorios, com a inclusão de um valor a semente será gerada com base nessa informação ex:(python gnl.py -s qualquercoisa) semente do programa irá gerar sempre os numeros [2,18,22,34,56,60]')
    parser.add_argument('-sc',dest='sementec',action='store',default='',required=False,help='Valor da sementeC opcional, por padrão o software gera uma aposta, se for inserido valor na sementeC o software ira gerar mais uma aposta com base na semente informada ex:(python gnl.py -sc 1900) indicando o concurso 1900 com esta opção o software ira gerar dois jogos, um com numero aleatorio devido o argumento -s não ter sido informado e o jogo [12,21,23,30,45,55]')
    parser.add_argument('-sd',dest='semented',action='store',default='',required=False,help='Valor da sementeD opcional, por padrão o software gera uma aposta, se for inserido valor na sementeD o software ira gerar mais uma aposta com base na semente informada ex:(python gnl.py -sc 1900 -sd 04022017) indicando o concurso 1900 e a data 04/02/2017 com esta opção o software ira gerar três jogos, um com numero aleatorio devido o argumento -s não ter sido informado e o jogo para o argumento -sc 1900 [12,21,23,30,45,55] e para o argumento -sd 04022017 [5,24,28,29,53,56]')
    parser.add_argument('-scd',dest='sementecd',action='store',default='',required=False,help='Valor da sementeCD opcional, por padrão o software gera uma aposta, se for inserido valor na sementeCD o software ira gerar mais uma aposta com base na semente informada ex:( python gnl.py -scd 190004022017 ) indicando o concurso 1900 e a data 04/02/2017 com esta opção o software ira gerar dois jogos um com numero aleatorio devido o argumento -s não ter sido informado e o jogo para o argumento -scd 190004022017 [18,22,28,35,52,53] ')
    parser.add_argument('-gn',dest='gerarnumeros',action='store',default='6',required=False,help='Argumento gerarNumeros opcional, insira a quantidade de numeros de sorteios a ser gerados, por padrão será gerados 6 sorteios ex:( python gnl.py -s teste -gn 10 )o software ira gerar 10 sorteios [3,12,21,29,32,34,36,37,53,57] OBS: Se um numero for sorteado mais de uma vez a lista não apresentará este numero duplicado,ex:( python gnl.py -s teste -gn 40 ) ira retornar 39 numeros uma que o numero 37 e sorteado duas vezes')
    parser.add_argument('-nm',dest='numerominimo',action='store',default='1', required=False,help='Argumento numerominimo opcional, por padrão o numero 1 e o menor numero para sorteio jogos como lotomania usam o (00 ou 0) em seus sorteios para gerar numeros com zero basta usar ex: ( python gnl.py -nm 0 ) um possivel resultado será [0,1,2,3,4,5] para gerar mais numeros para o sorteio use a opção -gn')
    parser.add_argument('-nma',dest='numeromaximo',action='store',default='60',required=False,help='Argumento numeroMaximo opcional, por padrão o numero 60 e o maior numero para sorteio jogos como lotomania usam o (99) para gerar sorteios com numeros até 99 usar ex: ( python gnl.py -nma 99 ) um possivel resultado será [94,95,96,97,98,99] para gerar mais numeros para o sorteio use a opção -gn e para incluir o 0 use -nm')
    parser.add_argument('-acm', dest='acertoMinimo', action='store', default='6', required=False,help='Argumento acertoMinimo a quantidade de numeros minimos para gerar premiação no concurso ex: ( python gnl.py -la lotomania -acm 15 -s qualquerCoisa -nm 0 -nma 99 -gn 30 ) ')
    parser.add_argument('-la',dest='arquivo', action='store', default='', required=False, help='Indica o nome do arquivo de texto que contem todos os jogos para serem analizados, o arquivo deve estar na mesma pasta do programa gnl.py, a formatação do arquivo deve conter (concurso,data,todosOsNumerosSeparadosComVirgula) ex: 1,02101999,16,11,88,32,25,0,70,78,73,61,90,89,46,95,6,33,34,21,14,22   Para a correta utilização deste parametro obrigatoriamente o paramentro -s deve ser usado')

    #Passando valores para as variaveis
    argumentos = parser.parse_args()
    var_semente = str(argumentos.semente)
    var_sementec = str(argumentos.sementec)
    var_semented = str(argumentos.semented)
    var_sementecd = str(argumentos.sementecd)
    var_arquivo = str(argumentos.arquivo)
    try:
        var_acertoMinimo = int(argumentos.acertoMinimo)
        var_gerarNumeros = int(argumentos.gerarnumeros)
        var_numeroMinimo = int(argumentos.numerominimo)
        var_numeroMaximo = int(argumentos.numeromaximo)
    except:
        print('Argumentos (-gn , -nm  , -nma ) Exigem numeros inteiros')
    os.system('cls')
    print("Analista de Sitemas: PRINCE, Klayton Bueno\n"
          " Programa gerador de numeros aleátorios ou fixos para jogos da loteria\n"
          "Semente-----------------: %s\n"
          "SementeC----------------: %s\n"
          "SementeD----------------: %s\n"
          "SementeCD---------------: %s\n"
          "Gerar Numeros-----------: %s\n"
          "Numero Inicial----------: %s\n"
          "Numero Final------------: %s\n"%(var_semente,
                                            var_sementec,
                                            var_semented,
                                            var_sementecd,
                                            str(var_gerarNumeros),
                                            str(var_numeroMinimo),
                                            str(var_numeroMaximo)))

    dic[1] = geradorSorteio(semente = var_semente, numeroMinimo=var_numeroMinimo, numeroMaximo=var_numeroMaximo, gerarNumeros=var_gerarNumeros)
    if var_sementec != '':
        dic[2] = geradorSorteio(semente=var_sementec, numeroMinimo=var_numeroMinimo, numeroMaximo=var_numeroMaximo, gerarNumeros=var_gerarNumeros)
    if var_semented != '':
        dic[3] = geradorSorteio(semente=var_semented, numeroMinimo=var_numeroMinimo, numeroMaximo=var_numeroMaximo, gerarNumeros=var_gerarNumeros)
    if var_sementecd != '':
        dic[4] = geradorSorteio(semente=var_sementecd, numeroMinimo=var_numeroMinimo, numeroMaximo=var_numeroMaximo, gerarNumeros=var_gerarNumeros)
    imprimirResultadoDicionario(dic)
    if var_arquivo != '':
        if var_semente != '':
            lerArquivo(var_arquivo, semente=var_semente, numeroMinimo=var_numeroMinimo, numeroMaximo=var_numeroMaximo, gerarNumeros=var_gerarNumeros, acertoMinimo=var_acertoMinimo)
        else:
            os.system('cls')
            print('O uso do paramentro -la exige que o paramentro -s seja  usado\n'
                  'A comparação ira altomaticamente percorrer todos os resultados\n'
                  'a fim de saber se o uso das sementes poderia ter  gerado algum\n'
                  'resultado favoravel para o usuário ')










if __name__ == "__main__":
    os.system('cls')
    gnl()
