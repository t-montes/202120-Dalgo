"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from os import getcwd
from helper import InC,Out,define,timer

@timer()
def overlap(w1:str, w2:str) -> tuple:
    1

@timer()
def min_str() -> str:
    1

def main():
    outs:list = []
    for words in InC():
        outs.append(min_str())
    Out(outs)

if __name__ == "__main__":
    define("C", getcwd())
    try:
        main()
    except Exception as e:
        errorargs = "\n\t- "+"\n\t- ".join([str(i) for i in e.args]) if len(e.args) > 1 else e.args[0]
        input(f'Raised {e.__class__.__name__}: {errorargs}')
