"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from os import getcwd
from helper import InC,Out,define,timer
from itertools import permutations

@timer()
def overlap(w1:str, w2:str) -> tuple:
    i = 0
    if w2 in w1: return w1,0
    elif w1 in w2: return w2,0
    while not w2.startswith(w1[i:]):
        i += 1
    return w1[:i]+w2, len(w1[:i])

@timer()
def min_str(words:list) -> str:
    mw:list = []
    perms = permutations(words)
    for p in perms:
        s:str = ""
        for i in range(1,len(p)):
            s = overlap(s, overlap(p[i-1],p[i])[0])[0]
        mw.append(s)
    w = min(mw, key=lambda u:len(u))
    return w

def main():
    outs:list = []
    for words in InC():
        outs.append(min_str(words))
    Out(outs)

if __name__ == "__main__":
    define("C", getcwd())
    try:
        main()
    except Exception as e:
        errorargs = "\n\t- "+"\n\t- ".join([str(i) for i in e.args]) if len(e.args) > 1 else e.args[0]
        input(f'Raised {e.__class__.__name__}: {errorargs}')