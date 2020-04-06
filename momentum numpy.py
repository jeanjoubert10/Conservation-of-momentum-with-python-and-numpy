import numpy as np

def momentum(aMass, bMass, aVel, bVel):

    aMom = aMass*aVel
    bMom = bMass*bVel


    a = np.array([[aMass, bMass],[1,-1]])
    b = np.array([aMom+bMom,bVel-aVel])


    x = np.linalg.solve(a,b)
    print(x)
    return x

value = momentum(5,4,6,-5)
print(value)
