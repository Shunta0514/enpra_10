import sympy as sp
if __name__=="__main__":
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    A = sp.cos(x)*sp.cos(x)+sp.sin(x)*sp.sin(x)
    A = sp.factor(A)
    print(A)
    