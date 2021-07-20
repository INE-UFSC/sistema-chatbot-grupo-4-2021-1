from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print("Olá, seja bem vindo ao nosso bate papo com bots! Só tome cuidado para não esquecer do mundo real.")

    def mostra_menu(self):
        print("Nós temos os seguintes BOTs disponíveis:")
        for i, bot in enumerate(self.__lista_bots):
            print(i, "-", bot.nome)
    
    def escolhe_bot(self):
        while True:
            ibot = input("Escolha o seu bot pelo número: ")
            try:
                ibot = int(ibot)
            except:
                print("O valor inserido deve ser um número")
                continue

            if ibot >= 0 and ibot < len(self.__lista_bots):
                self.__bot = self.__lista_bots[ibot]
                break
            else:
                print("Não há um bot com esse número")

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())

    def le_envia_comando(self):
        cmd = input("Insira o comando, ou insira -1 para sair")
        if cmd == "-1":
            return False
        self.__bot.executa_comando(cmd)

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.__bot.boas_vindas()
        while True:
            print(self.mostra_comandos_bot)
            if not self.le_envia_comando:
                break
        self.__bot.despedida()

