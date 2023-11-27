
"""
Euler-Maruyama Method For SDEs
"""
import numpy as np
import matplotlib.pyplot as plt


# Define drift and volitility
def b(x,t):
    return x

def sigma(x,t):
    return t

T= 5  # final t-value
x0=1  # initial position
dt =.05 # time increment
N=1000 # number of sample paths


t_vals = np.arange(0,T,dt)
num_t_vals= len(t_vals)
x_vals=np.zeros((num_t_vals,N))

x_vals[0,:] = x0

for n in range(N-1):
    for i in range(1,len(t_vals)):
        dWt = np.random.normal(0,dt)
        x_vals[i,n] = x_vals[i-1,n]+ b(x_vals[i-1,n],t_vals[i-1])*dt + sigma(x_vals[i-1,n],t_vals[i-1])*dWt

# Plot sample paths
for i in range(5):
    lab = "path "+str(i)
    plt.plot(t_vals,x_vals[:,i],label = lab)

plt.show

# Plot histogram at final time
n_bins=20
fig, axs = plt.subplots(1, 1)
 

axs.hist(x_vals[-1,:], bins = n_bins)
plt.show







