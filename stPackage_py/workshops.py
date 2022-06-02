import requests

#Primer ENTPOINT
#definimos una función que va a realizar la peticion y retorna un JSON
def unreleased():
    """Retorna los próximos talleres en CódigoFacilito
    >>> type(unreleased()) == type(dict())
    True
    """                 #obtenemos el tipo de la funcion y si es igual al tipo diccionario regresa True

    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')

    if response.status_code == 200:     #si fue correcta
        payload = response.json()      #convertimos lo que retorma en un diccionario
        return payload['data']         #en data existe el listado de workshops