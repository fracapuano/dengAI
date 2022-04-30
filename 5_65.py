h = []
g = []


def f(x):
    return (x[0]-x[1])**2 + ((x[0] + x[1] - 10.)**2)/9 + (x[2] - 5.)**2



def g1(x):
    return -(48. - x[0]**2 - x[1]**2 - x[2]**2)
g.append(g1)



def g2s(x):
    return -(x[0] + 4.5)
g.append(g2s)



def g2d(x):
    return (x[0] - 4.5)
g.append(g2d)



def g3s(x):
    return -(x[1] + 4.5)
g.append(g3s)



def g3d(x):
    return (x[1] - 4.5)
g.append(g3d)




def g4s(x):
    return -(x[2] + 5.)
g.append(g4s)



def g4d(x):
    return (x[2] - 5.)
g.append(g4d)



x0 = np.array([-5., 5., 0.])


#x*=(3.65, 3.65 , 4.62 ) f(x*) = 0.95



#CONVERGE (GD_mod & NT)