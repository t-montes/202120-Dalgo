"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from os import getcwd
from helper import InA,Out,define,timer

@timer()
def fill_r(n:int, A:float, B:float, C:float, D:float) -> list:
    """Llena la lista r con los elementos necesarios para el cálculo"""
    r = []
    r.append(A)
    r.append(B)
    for k in range(2,n+1):
        r.append(D*r[k-1] + C*r[k-2])
    return r

@timer()
def cp(r:list, n:int) -> float:
    """Retorna el cálculo de la convolución ponderada dados r,n"""
    x:float = 0.0
    for k in range(0,n+1):
        x += r[k]*r[n-k]
        if k >= (n/2 - 1): break
    x *= 2
    x += r[n//2]**2 if n%2==0 else 0
    return x

def main():
    outs:list = []
    for n,A,B,C,D in InA(int,float,float,float,float):
        r = fill_r(n,A,B,C,D)
        outs.append(cp(r,n))
    Out(outs)

if __name__ == "__main__":
    define("A", getcwd())
    try:
        main()
    except Exception as e:
        errorargs = "\n\t- "+"\n\t- ".join([str(i) for i in e.args]) if len(e.args) > 1 else e.args[0]
        input(f'Raised {e.__class__.__name__}: {errorargs}')
    
