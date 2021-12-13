"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from os import getcwd
from helper import InB,Out,define,timer,Graph

def get_next_not_coloured(direct:set, edges:list):
    """It will never no-return"""
    for a,b in edges:
        if a in direct:
            return b
        if b in direct:
            return a

@timer()
def dif_graph(g:Graph) -> int:
    """Agrupa el grafo en 2 subgrafos que lo hacen bipartito y retorna el diferencial"""
    n:int = len(g.v)
    l1,coloured = 0,set()
    while g.v:
        if l1: v,l1 = get_next_not_coloured(coloured, g.e),l1+1
        else:  v,l1 = 0,1
        g.v.discard(v)
        i:int = 0
        while i < len(g.e):
            a,b = g.e[i]
            if v==a:
                coloured.add(b)
                g.v.discard(b)
                del g.e[i]
            elif v==b:
                coloured.add(a)
                g.v.discard(a)
                del g.e[i]
            else:
                i += 1
    df = abs(len(coloured)-l1)
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
