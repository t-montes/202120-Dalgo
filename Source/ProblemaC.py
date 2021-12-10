"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from helper import Out,define

def In():
    #inputs for problem C are different
    ...

def main():
    outs:list = []
    for inputs in In():
        ...
    Out(outs)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        errorargs = "\n\t- "+"\n\t- ".join(e.args) if len(e.args) > 1 else e.args[0]
        print(f'Raised {e.__class__.__name__}: {errorargs}')
