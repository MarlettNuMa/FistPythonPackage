#import stPackage           -importa todo el paquete
from stPackage_py.workshops import unreleased       #importa una funcion

if __name__ == '__main__':
    #print('Hola Mundo :D :P.')
    workshops = unreleased()
    print(workshops)