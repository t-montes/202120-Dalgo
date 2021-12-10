"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from helper import In,Out,define

global r

def fill_r(n:int, A:float, B:float, C:float, D:float) -> float:
    global r
    r = []
    r.append(A)
    r.append(B)
    for k in range(2,n+1):
        r.append(D*r[k-1] + C*r[k-2])

def cp(n:int) -> float:
    global r
    x:float = 0.0
    for k in range(0,n+1):
        x += r[k]*r[n-k]
        if k >= (n/2 - 1): break
    x *= 2
    return x+(r[n//2]**2) if n%2==0 else x

def main():
    outs:list = []
    for n,A,B,C,D in In(int,float,float,float,float):
        fill_r(n,A,B,C,D)
        outs.append(cp(n))
    Out(outs)

if __name__ == "__main__":
    define("A")
    try:
        main()
    except Exception as e:
        errorargs = "\n\t- "+"\n\t- ".join(e.args) if len(e.args) > 1 else e.args[0]
        input(f'Raised {e.__class__.__name__}: {errorargs}')
        
