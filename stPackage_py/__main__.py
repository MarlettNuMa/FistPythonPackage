import logging
from stPackage_py import unreleased         #con unreleased inicializada en init

"""
MESSAGE INTO LOGGING
1)INFO
2)DEBUG
3)WARNING
4)ERROR
5)CRITICAL

logging.basicConfig(level=logging.DEBUG)
    muestra mensajes de 20 a superiores
"""

logging.basicConfig(level = logging.INFO)

"""     Sin usar DOCSTRINGS
if __name__ == '__main__':
    logging.debug('>>>  Ejecución del paquete iniciada')
    
    workshops = unreleased()
    print(workshops)

    logging.debug('>>> Finalizada la ejecución del paquete')
"""

"""Usando DOSCTRINGS
if __name__ == '__main__':
    logging.debug('>>>  Ejecución del paquete iniciada')
    
    workshops = unreleased()

    logging.debug(unreleased())
    #logging.debug(unreleased.__doc__)  En vez de ver los workshops
    #logging.debug(help(unreleased))    Es otra forma de hacerlo

    logging.debug('>>> Finalizada la ejecución del paquete')
"""

#usando entry_points

def main():
    logging.info(unreleased())


if __name__ == '__main__':
    logging.debug('>>>  Ejecución del paquete iniciada')

    main()

    logging.debug('>>> Finalizada la ejecución del paquete')