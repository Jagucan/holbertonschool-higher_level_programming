#!/usr/bin/python3
""" Module that returns the list
    of available attributes
"""
def lookup(objeto):
    """ Returns the list of available attributes
        and methods of an object
    """
    resultado = []
    for atributo in dir(objeto):
        if not atributo.startswith('__'):
            resultado.append(atributo)
    return resultado
