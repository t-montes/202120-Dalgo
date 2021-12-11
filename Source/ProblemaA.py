"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""
from helper import In,Out,define,timer

global r

@timer()
def fill_r(n:int, A:float, B:float, C:float, D:float):
    global r
    r = []
    r.append(A)
    r.append(B)
    for k in range(2,n+1):
        r.append(D*r[k-1] + C*r[k-2])

@timer()
def cp(n:int) -> float:
    x:float = 0.0
    for k in range(0,n+1):
        x += r[k]*r[n-k]
        if k >= (n/2 - 1): break
    x *= 2
    x += r[n//2]**2 if n%2==0 else 0
    return x

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
        input()
    except Exception as e:
        errorargs = "\n\t- "+"\n\t- ".join([str(i) for i in e.args]) if len(e.args) > 1 else e.args[0]
        input(f'Raised {e.__class__.__name__}: {errorargs}')
    
