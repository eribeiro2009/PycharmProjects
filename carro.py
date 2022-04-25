class Carro():
    """Esta é a classe CARRO utilizada para criar novos carros"""
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado, velocidade):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado
        self.velocidade = velocidade


    def abastecer(self, qtd_combustivel=10):
        """Método utilizado para acrescentar combustivel"""
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado:
            print('Carro já está ligado')
        else:
            self.is_ligado = True
            print("Ligando o carro...")

    def desligar(self):
        if self.is_ligado == False:
            print('Carro já está desligado')
        else:
            self.is_ligado = False
            self.velocidade = 0
            print("Desligando o carro...")

    def acelear(self, velocidade=10):
        if self.is_ligado == True:
            self.velocidade += velocidade
            print("Acelerando o carro...")
        else:
            print("Carro não pode ser acelerado pois está DESLIGADO!")