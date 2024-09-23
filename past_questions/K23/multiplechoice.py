a = 0

def f(x):
    global a
    print(x)
    a = 1
    print(x)
    x = 2

def q1():
    f(a)
    print(a)

q1()


L = [0, 1]

def g(M):
    global L
    L = [2, 3]
    print(M[0][0])
    M[1][1] = 4
    print(M[0][1])

def q2():
    g([L] * 2)
    print(L[1])


q2()
