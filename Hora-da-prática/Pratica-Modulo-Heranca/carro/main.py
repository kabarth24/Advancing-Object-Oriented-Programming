from carro import Carro
from moto import Moto

carro1 = Carro('Chevrolet', 'Onix 1.0 Turbo Flex Premier', 4)
carro2 = Carro('Volkswagen', 'Golf 2.0 TSI GTI DSG', 4)

moto1 = Moto('Yamaha', 'MT-03 ABS', 'Esportiva')
moto2 = Moto('Harley-Davidson', 'Street 750', 'Esportiva')

def main():
    print(carro1)
    print(carro2)
    print(moto1)
    print(moto2)

if __name__ == '__main__':
    main()