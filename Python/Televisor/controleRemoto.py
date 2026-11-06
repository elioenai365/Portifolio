class ControleRemoto:
    def __init__(self,tv):

        self.tv = tv

    def aumentarVolume (self):
        self.tv.aumentarVolume(90)
    def diminuirVolume (self):
        self.tv.diminuirVolume(90)
    def trocaCanal(self,canal):
        self.tv.trocaCanal(canal)
    def sintonizarCanal(self,canal):
        self.tv.sintonizarCanal(canal)