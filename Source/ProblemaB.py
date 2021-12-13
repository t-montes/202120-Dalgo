"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from os import getcwd
from helper import InB,Out,define,timer,Graph

@timer()
def dif_graph(g:Graph) -> int:
    """Agrupa el grafo en 2 subgrafos que lo hacen bipartito y retorna el diferencial"""
    l1:int = 0
    n:int = len(g.v)
    while g.v:
        v,l1 = g.v.pop(),l1+1
        i:int = 0
        while i < len(g.e):
            a,b = g.e[i]
            if v==a:
                g.v.discard(b)
                del g.e[i]
            elif v==b:
                g.v.discard(a)
                del g.e[i]
            else:
                i += 1
    df = abs(n - 2*l1)
    return df

@timer()
def min_dif(d:list) -> int:
    d.sort()
    s_pos:int = sum(d)
    s_neg:int = -s_pos
    while d:
        i:int = 2*d.pop()
        if  i <= s_pos: s_pos -= i
        elif i > s_neg: s_neg = s_pos-i
    m = min(s_pos,abs(s_neg))
    return m

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
