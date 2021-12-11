from time import process_time as _process_time
global _name

def define(name:str):
    global _name
    _name = name

def InA(*parsetypes) -> tuple:
    with open(f"./A.in",'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            if data[i] == "0": break
            spl:list = data[i].split()
            assert len(spl) == len(parsetypes), f"\n  Error reading input on line {i+1}\n  Expected {len(parsetypes)} arguments but got {len(spl)}"
            yield [parsetypes[i](spl[i]) for i in range(0,len(spl))]

def InB(*parsetypes) -> tuple:
    ...

def InC(*parsetypes) -> tuple:
    ...

def Out(outs:list):
    print(*outs,sep="\n")
    with open(f"./{_name}.out",'w') as file:
        file.write('\n'.join([str(o) for o in outs]))

def timer(format:str="El tiempo que tardó la funcion %s fue de %f segundos."):
    """Decorador que permite medir el tiempo en segundos que tarda una función.
        El parámetro opcional es el formato de impresión del tiempo (debe contener almenos un '%s')"""
    def decorator(func):
        def inner(*args, **kwargs):
            t1 = _process_time()
            ret = func(*args, **kwargs)
            t2 = _process_time()
            if format:
                print(format%((func.__name__, t2-t1) if "%s" in format else (t2-t1,)))
            return ret
        return inner
    return decorator
