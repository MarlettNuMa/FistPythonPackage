#import stPackage           -importa todo el paquete
#from stPackage_py.workshops import unreleased       #importa una funcion sin inicializarla en init
from stPackage_py import unreleased         #con unreleased inicializada en init

if __name__ == '__main__':
    #print('Hola Mundo :D :P.')
    workshops = unreleased()
    print(workshops)