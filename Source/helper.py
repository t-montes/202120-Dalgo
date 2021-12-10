global __name

def define(name:str):
    global __name
    __name = name

def In(*parsetypes) -> tuple:
    with open(f"./{__name}.in",'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            if data[i] == "0": break
            spl:list = data[i].split()
            assert len(spl) == len(parsetypes), f"\n  Error reading input on line {i+1}\n  Expected {len(parsetypes)} arguments but got {len(spl)}"
            yield [parsetypes[i](spl[i]) for i in range(0,len(spl))]

def Out(outs:list):
    print(*outs,sep="\n")
    with open(f"./{__name}.out",'w') as file:
        file.write('\n'.join([str(o) for o in outs]))
