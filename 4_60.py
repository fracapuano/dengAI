g = []
h = []

def h1(x):
    return x[0]*(1+x[1]**2)+x[2]**4-4-3*(2**0.5)
h.append(h1)



def g1(x):
    return x[0]-10
g.append(g1)



def g2(x):
    return -(x[0]+10)
g.append(g2)



def g3(x):
    return -(x[1]+10)
g.append(g3)



def g4(x):
    return -(x[2]+10)
g.append(g4)



def g5(x):
    return (x[1]-10)
g.append(g5)



def g6(x):
    return (x[2]-10)
g.append(g6)




x0 = np.array([2.,2.,2.])


#(1.10486,1.19667,1.5352) f(x*) = 0.032568

#CONVERGE (GD_mod & NT)