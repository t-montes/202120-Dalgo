"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from helper import InB,Out,define,timer

def main():
    outs:list = []
    for inputs in InB():
        ...
    Out(outs)

if __name__ == "__main__":
    define("B")
    try:
        main()
    except Exception as e:
        errorargs = "\n\t- "+"\n\t- ".join(e.args) if len(e.args) > 1 else e.args[0]
        print(f'Raised {e.__class__.__name__}: {errorargs}')
