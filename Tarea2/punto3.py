
def function(a,b,q,r):
    assert b > 0, "Precondition"
    
    q,r = 0,a

    while r >= b:
        assert b > 0 and a == q*b + r, "Invariant"
        q,r = q+1, r-b

    assert a == q*b + r and r < b, "Postcondition"

    print(a,b,q,r)

function(7,2,0,0)
