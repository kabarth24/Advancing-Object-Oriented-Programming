from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Suco de Melancia', 5, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa1 = Sobremesa('Sorvete de Brownie', 10, 'Doce', 'Médio')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa1)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()