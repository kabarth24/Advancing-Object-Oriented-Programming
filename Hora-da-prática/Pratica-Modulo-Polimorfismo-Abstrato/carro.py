from veiculo import Veiculo

class Carro(Veiculo):
  def __init__(self, marca, modelo, cor):
    super().__init__(marca, modelo)
    self.cor = cor

  def __str__(self):
    return f'{super().__str__()} | Cor: {self.cor}'

  def ligar(self):
    pass