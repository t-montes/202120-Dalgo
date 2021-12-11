"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from os import getcwd
from helper import InB,Out,define,timer

def dif_graph(graph:tuple) -> int:
    """Agrupa el grafo en 2 subgrafos que lo hacen bipartito y retorna el diferencial"""
    ...

def min_dif(difs:list) -> int:
    """Dados los diferenciales de todos los grafos (difs) hallar el mínimo diferencial del BC-Suma"""
    ...

def main():
    outs:list = []
    for graphs in InB():
        difs:list = []
        for g in graphs:
            difs.append(dif_graph(g))
        outs.append(min_dif(difs))
    Out(outs)

if __name__ == "__main__":
    define("B", getcwd())
    try:
        main()
    except Exception as e:
        errorargs = "\n\t- "+"\n\t- ".join([str(i) for i in e.args]) if len(e.args) > 1 else e.args[0]
        input(f'Raised {e.__class__.__name__}: {errorargs}')
