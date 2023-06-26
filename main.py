# Simulation of interacting einstein solids
from einstein import EinsteinSolid
import numpy as np
import matplotlib.pyplot as plt
import math

# System of Einstein Solids

# Total number of einstein solids
N_solids = 2

# Dont add more than 2 solids, otherwise numbers get too big

# Total amount of energy in the system
q_total = 300

# Oscillators per einstein solid
n_oscillators = 300

# WARNING: the program breaks down at parameters ~>1000. 

# Boltzmann Constant
k=1

def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation

# Every possible microstate of a system given N oscillators and k energy units
macrostates = list(sums(N_solids,q_total))

# Total macrostates
print(f"Total macrostates of a system given {N_solids} solids and {q_total} energy units: ", len(macrostates))

S_dist = np.empty(len(macrostates))
total_ms_dist = np.empty(len(macrostates), dtype=np.float128)

n=0

# Calculate microstates for each macrostate
for macrostate in macrostates:
    ms = np.array([EinsteinSolid(n_oscillators).getMicroStates(energy_of_solid) for energy_of_solid in macrostate])
    # Total microstates
    total_ms = np.prod(ms)
    # Entropy calculation
    S = k*math.log(total_ms)
    
    S_dist[n] = S
    total_ms_dist[n]=total_ms
    n+=1

    #print("Macrostate: ", macrostate)    
    #print("Total Microstates: ",total_ms)
    #print("Entropy of macrostate: ", round(S,2))
    #print()

plt.figure(1)
plt.bar(np.arange(0,len(macrostates)),total_ms_dist)
plt.title("Multiplicity vs q_A")

plt.figure(2)
plt.bar(np.arange(0,len(macrostates)),S_dist)
plt.title("Entropy vs q_A")

plt.show()