import numpy as np

class EinsteinSolid:
    def __init__(self,n_oscillators):
        self.n_oscillators = n_oscillators
        
    # Return the number of microstates of a given macrostate (specified by number of energy units)
    def getMicroStates(self,q):
        return np.math.factorial(q+self.n_oscillators-1)//(np.math.factorial(q)*np.math.factorial(self.n_oscillators-1))