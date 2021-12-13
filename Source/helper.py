from os import getcwd as _getcwd
from time import process_time_ns as _process_time_ns
global _name
global _dir

def timer(format:str="El tiempo que tardó la funcion %s fue de %.9f segundos."):
    """Decorador que permite medir el tiempo en segundos que tarda una función.
        El parámetro opcional es el formato de impresión del tiempo (debe contener almenos un '%f')"""
    def decorator(func):
        def inner(*args, **kwargs):
            t1 = _process_time_ns()/1e9
            ret = func(*args, **kwargs)
            t2 = _process_time_ns()/1e9
            if format:
                print(format%((func.__name__, t2-t1) if "%s" in format else (t2-t1,)))
            return ret
        return inner
    return decorator

def define(name:str, dir:str):
    global _name, _dir
    _name, _dir = name, dir

def split(a:list, n:int):
    """Splits list a into n approximately equal parts"""
    if n == 0: return []
    k, m = divmod(len(a), n)
    return list(a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

class Graph():
    def __init__(self, vertices:set, edges:list):
        self.v = vertices
        self.e = edges

def InA(*parsetypes) -> tuple:
    path:str = f"{_dir}\\A.in"
    with open(path,'r') as file:
        data:list = file.readlines()
        for i in range(len(data)):
            if data[i] == "0": break
            spl:list = data[i].split()
            assert len(spl) == len(parsetypes), f"\n  {path}\n  Error reading input on line {i+1}\n  Expected {len(parsetypes)} arguments but got {len(spl)}"
            yield [parsetypes[i](spl[i]) for i in range(0,len(spl))]

def InB() -> tuple:
    path:str = f"{_dir}\\B.in"
    with open(path,'r') as file:
        data:list = file.readlines()
        n:int = int(data[0])
        graphs:list = []
        for i in range(1,len(data)):
            if n == 0:
                yield graphs
                n = int(data[i])
                if n == 0: break
                graphs = []
            else:
                spl:list = [int(j) for j in data[i].split()]
                assert len(spl) >= 2, f"\n  {path}\n  Error reading input on line {i+1}\n  Expected at least 2 arguments |v|,|e| but got {len(spl)}"
                assert len(spl) == 2*(spl[1]+1), f"\n  Error reading graph on line {i+1}\n  Expected {spl[1]} edges but got {len(spl)/2 - 2}"
                v,e = set(j for j in range(spl[0])),split(spl[2:],spl[1])
                graphs.append(Graph(v,e))
                n -= 1

def InC(*parsetypes) -> tuple:
    ...

def Out(outs:list):
    print(*outs,sep="\n")
    path:str = f"{_dir}\\{_name}.out"
    with open(path,'w') as file:
        file.write('\n'.join([str(o) for o in outs]))
