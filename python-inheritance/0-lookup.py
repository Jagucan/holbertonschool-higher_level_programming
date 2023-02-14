#!/usr/bin/python3
def lookup(objeto):
    """ Devuelve una lista de atributos y
        métodos disponibles de un objeto.
    """
    resultado = []
    for atributo in dir(objeto):
        if not atributo.startswith('__'):
            resultado.append(atributo)
    return resultado
