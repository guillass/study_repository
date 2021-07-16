class Carrinho:
    def __init__(self):
        self.itens = []
        #self.total = 0
        
    
    def add(self,item):
        self.itens.append(item)
        #self.total = self.total +item.valor


    def get_total(self):
        resultado = 0
        for current_item in self.itens:
            resultado = resultado + current_item.valor
        return resultado



class Item:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor