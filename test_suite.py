import unittest
from carrinho import Carrinho,Item 


class ClasseTeste(unittest.TestCase):
    
    def test_deve_calcular_total_de_compras(self):
        cesta = Carrinho() 
        cesta.add(Item("cigarro",5))
        cesta.add(Item("pitu",6))
        cesta.add(Item("coca",5))
        self.assertEqual(cesta.get_total(),16)


    def test_se_valor_de_um_item_for_alterado_total_deve_ser_alterado(self):
        item_unico = Item("Gasolina",7)
        cesta = Carrinho() 
        cesta.add(item_unico)
        cesta.add(Item("cigarro",5))
        cesta.add(Item("pitu",6))
        cesta.add(Item("coca",5))
        self.assertEqual(cesta.get_total(),23)
        item_unico.valor = 9
        self.assertEqual(cesta.get_total(),25)



if __name__ == '__main__':
    unittest.main()

