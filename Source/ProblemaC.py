"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from helper import InC,Out,define,timer

def main():
    outs:list = []
    for inputs in InC():
        ...
    Out(outs)

if __name__ == "__main__":
    define("C")
    try:
        main()
    except Exception as e:
        errorargs = "\n\t- "+"\n\t- ".join([str(i) for i in e.args]) if len(e.args) > 1 else e.args[0]
        input(f'Raised {e.__class__.__name__}: {errorargs}')
