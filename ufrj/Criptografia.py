'''
            Universidade Federal do Rio de Janeiro
         Centro de Ciências Matemáticas e da Natureza
        Bacharelado em Ciências Matemáticas e da Terra

            Desenvolvedor(es): Hugo Miranda e Souza
            DRE: 118043403

            Professora: Lenka Ptackova
            Disciplina: [MAB241] Computação II

            Descrição: Lista de exercicio nº6, criptografia e descriptografia
                de mensagens e conteudo de arquivos.
                Disponivel em: https://dcc.ufrj.br/~pythonufrj/python2.html
            Python Version: 3.7.3
            Data: 01/10/2019
'''


class Criptografia():
    def __init__(self):
        # Inicializa no construtor os caracteres que podem criptografados
        self.CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%abcdefghijklmnopqrstuvwxyz"

    def criptografar(self, letra, k):
        if not -70 <= k < 70:  # Caso K(chave) esteja fora dos limites dos caracteres que podem ser criptografados
            return 0  # sai do metodo
        CARACTERES = self.CARACTERES  # Atribui a CARACTERES a lista de caracteres que podem ser criptografados

        if letra in CARACTERES:  # se a letra puder ser criptografada
            pos_letra = CARACTERES.index(letra)  # seleciona o index em CARACTERES
            new_pos_letra = pos_letra + k  # Seleciona a nova posição somando K ao index obtido
            if pos_letra + k >= len(CARACTERES):  # caso a soma seja maior que o tamanho de CARACTERES
                new_pos_letra -= len(CARACTERES)  # é posição é subtraida do total de caracteres (retorna ao inicio)
                # ex: criptografar("z", 1) retorna 'A'
            return CARACTERES[new_pos_letra]  # retorna a letra criptografada
        else:  # Caso a letra nao esteja em CARACTERES
            return letra  # retorna a propria letra

    def descriptografar(self, letra, k):
        if not -70 <= k < 70:  # Caso K(chave) esteja fora dos limites dos caracteres que podem ser criptografados
            return 0  # sai do metodo
        CARACTERES = self.CARACTERES  # Atribui a CARACTERES a lista de caracteres que podem ser criptografados

        if letra in CARACTERES:  # se a letra puder ser criptografada
            pos_letra = CARACTERES.index(letra)  # seleciona o index em CARACTERES
            new_pos_letra = pos_letra - k  # Seleciona a nova posição somando K ao index obtido
            if pos_letra - k >= len(CARACTERES):  # caso a soma seja maior que o tamanho de CARACTERES
                new_pos_letra -= len(CARACTERES)  # é posição é subtraida do total de caracteres (retorna ao inicio)
                # ex: descriptografar("A", 1) retorna 'z'
            return CARACTERES[new_pos_letra]  # retorna a letra descriptografada
        else:  # Caso a letra nao esteja em CARACTERES
            return letra  # retorna a propria letra

    # criptografia de arquivo
    def f_criptografar(self, file_name="", k=0):
        new_message = ""
        try:
            file = open(file_name, "r")  # abre o arquivo para leitura
            file_extension = file_name.index(".")  # seleciona o index do inicio da extensao do arquivo
            # Adiciona, antes da extensao a string "Cripto", ex: "ArquivoCripto.txt"
            new_file_name = file_name[:file_extension] + "Cripto" + file_name[file_extension:]
            file_cripto = open(new_file_name, "w")
            for letter in file.read():  # Para cada letra no arquivo
                new_letter = self.criptografar(letter, k)  # é feita a criptografia
                new_message += new_letter  # e adicionada a uma string contendo todas as letras criptografadas

            file_cripto.write(new_message)  # Escreve a mensagem criptografada no arquivo

            # Fechando os arquivos.
            file.close()
            file_cripto.close()

            # Se nao houver nenhum problema até aqui é printado uma mensagem de sucesso para a operação
            print("Procedimento de criptografia concluido.\nArquivo criptografado: {}".format(new_file_name))
        except FileNotFoundError:
            print("O arquivo não existe ou seu nome foi digitado incorretamente.")
        except IOError:
            print("Não foi possivel escrever no arquivo.")
        except TypeError:
            print("O valor de K está fora dos limites (-70 a 70)")

    # file overwrite: Sobrescrever arquivo com criptografia
    def fow_criptografar(self, file_name="", k=0):
        new_message = ""
        try:

            file = open(file_name, "r+")  # abre o arquivo para leitura e escrita
            for letter in file.read():  # Para cada letra no arquivo
                new_letter = self.criptografar(letter, k)  # é feita a criptografia
                new_message += new_letter  # e adicionada a uma string contendo todas as letras criptografadas

            file.seek(0)  # Retorna ponteiro para o inicio do arquivo
            file.write(new_message)  # Escreve a mensagem criptografada no arquivo

            # Fechando o arquivo.
            file.close()

            # Se nao houver nenhum problema até aqui é printado uma mensagem de sucesso para a operação
            print(
                "Procedimento de sobrescrita de arquivo com criptografia concluido.\nArquivo criptografado: {}".format(
                    file_name))
        except FileNotFoundError:
            print("O arquivo não existe ou seu nome foi digitado incorretamente.")
        except IOError:
            print("Não foi possivel escrever no arquivo.")
        except TypeError:
            print("O valor de K está fora dos limites (-70 a 70)")

    # descriptografia de arquivo
    def f_descriptografar(self, file_name, k):
        new_message = ""
        try:
            file = open(file_name, "r")  # abre o arquivo passado pelo parametro no modo leitura

            # Procura pela string "Cripto" no nome do arquivo
            if file_name.find("Cripto") > 0:  # caso ache a string no nome
                file_pos_strCripto = file_name.index("Cripto")  # seleciona o index onde começa a string "Cripto"
                # Inclui um "Des" antes de "Cripto" e troca "C" por "c", tornando "Descripto"
                new_file_name = file_name[:file_pos_strCripto] + "Des" + file_name[
                    file_pos_strCripto].lower() + file_name[file_pos_strCripto + 1:]
            else:  # Caso não encontre a string "Cripto"
                file_extension = file_name.index(".")  # seleciona o index onde começa a string de extensao do arquivo
                # E adiciona "Descripto" antes dela.
                new_file_name = file_name[:file_extension] + "Descripto" + file_name[file_extension:]

            # Cria o novo arquivo com a string "Descripto", ex: "ArquivoDescripto.txt"
            # no modo de escrita.
            file_descripto = open(new_file_name, 'w')

            for letter in file.read():  # Para cada letra do arquivo
                new_letter = self.descriptografar(letter, k)  # é feita a descriptografia
                new_message += new_letter  # e adicionada a uma string contendo todas as letras descriptografadas

            file_descripto.write(new_message)  # Escreve a mensagem descriptografada no novo arquivo

            # Fechando os arquivos.
            file.close()
            file_descripto.close()

            # Se nao houver nenhum problema até aqui é printado uma mensagem de sucesso para a operação
            print("Procedimento de descriptografia concluido.\nArquivo descriptografado: {}".format(new_file_name))
        except FileNotFoundError:
            print("O arquivo não existe ou seu nome foi digitado incorretamente.")
        except IOError:
            print("Não foi possivel escrever no arquivo.")
        except TypeError:
            print("O valor de K está fora dos limites (-70 a 70)")
