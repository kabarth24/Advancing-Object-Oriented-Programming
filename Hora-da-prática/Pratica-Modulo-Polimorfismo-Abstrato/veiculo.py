from abc import ABC, abstractmethod

class Veiculo(ABC):
  @abstractmethod
  def ligar(self):
    pass

  def __str__(self):
    return f'Marca: {self.marca} | Modelo: {self.modelo}'

  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
  