"""@author: Tony Santiago Montes Buitrago (santiago.montesb@gmail.com)"""

#Punto 1

def subConjuntoIgualASuma(a: list, T: int)->bool:
    m = []
    for i in range(len(a)+1):
        row = []
        for i in range(T+1):
            row.append(False)
        m.append(row)

    for i in range(len(m)):
        for j in range(len(m[i])):
            if j == 0:
                m[i][j] = True
            elif i == 0:
                m[i][j] = False
            else:
                if j-a[i-1] < 0:
                    m[i][j] = m[i-1][j]
                else:
                    m[i][j] = m[i-1][j-a[i-1]] or m[i-1][j]
    return m[len(m)][len(m)[0]]

#Punto 2

def matrixOnes(x:list):
    N,M=len(x),len(x[0])
    mtx = [[x[i][j]
            for j in range(M)] 
            for i in range(N)] #crea matrix de ceros
    i,j,run_i,tmp = 0,1,True,1
    while True:
        i,j = (i+1,j) if run_i else (i,j+1)
        if i>=N or j>=M: break

        if x[i][j]==0:
            r = 0
        else:
            if x[i-1][j] == x[i][j-1] == x[i-1][j-1] == 1:
                if mtx[i-1][j] == mtx[i][j-1] == mtx[i-1][j-1]:
                    r = mtx[i-1][j] + 1
                else:
                    r = max(mtx[i-1][j], mtx[i][j-1], mtx[i-1][j-1])
            else:
                r = x[i][j]
        mtx[i][j] = r

        if i==N-1:
            run_i,i,tmp = False,tmp,j+1
        if j==M-1:
            run_i,j,tmp = True,tmp,i+1
    
    return max([max(k) for k in mtx])

#Punto 3

def base4nums(N:int):
    lst = []
    i = -1
    while (i := i+1) <= N:
        if i==0:
            r = 1
        elif i==1:
            r = 4
        else:
            r = 3*(lst[i-1]+lst[i-2])
        lst.append(r)
    return lst[N]

#Punto 4

def _lC1(e:list, lstleft:list, i:int):
    if i==0:
        r = (2 if e[0]>e[1] else 1)
    else:
        if e[i]<e[i-1]:
            r = 1
        elif e[i]>e[i-1]:
            r = lstleft[i-1] + 1
        else:
            r = lstleft[i-1]
    lstleft.append(r)

def _lC2(e:list, lstright:list, i:int):
    if i==len(e)-1:
        r = (2 if e[len(e)-1]>e[len(e)-2] else 1)
    else:
        if e[i]<e[i+1]:
            r = 1
        elif e[i]>e[i+1]:
            r = lstright[i+1] + 1
        else:
            r = lstright[i+1]
    lstright[i] = r

def lessCandies(e:list):
    lstleft = []
    lstright = [0 for i in range(len(e))]
    i = -1
    while (i := i+1) < len(e):
        _lC1(e,lstleft,i)
    i = len(e)
    while (i := i-1) >= 0:
        _lC2(e,lstright,i)
    i,sum = -1,0
    while (i := i+1) < len(e):
        sum += max(lstleft[i], lstright[i])
    return sum

#Punto 5

def Nmeters(c:list):
    b = [None for i in range(len(c))]
    i = len(c)
    while (i := i-1) >= 0:
        if (c[i]==-1) or (i+c[i]>=len(c)):
            r = False
        elif (i==len(c)-1) and (c[i]==0):
            r = True
        else:
            r = b[i+1] or b[i+c[i]]
        b[i] = r
    return b[0]

def main():
    """Write here your tests"""
    

if __name__ == "__main__":
    main()
