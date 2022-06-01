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

logging.basicConfig(level = logging.DEBUG)


if __name__ == '__main__':
    logging.debug('>>>  Ejecución del paquete iniciada')
    
    workshops = unreleased()
    print(workshops)

    logging.debug('>>> Finalizada la ejecución del paquete')