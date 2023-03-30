# Use Mathematica to solve the two differential equations simultaneously. 
 #   dCA/dt = -k1CACB
  #   dCB/dt = -2k1CACB
# Initial conditions: at t = 0,   CA0 = 10,   CB0 = 12,   k1 = 0.
# The following packages must exist in your Python environment in order

# to plot solutions to differential equations in Python:

# – scipy

# – matplotlib

# The following 27 lines of code attempt to open these packages, and download them if you do not already have them.

# Note that if you use Anaconda or a similar Python distribution, then you likely already have these packages and

# would replace all of this code with these four lines:

# from scipy.integrate import odeint

# import numpy as np

# import matplotlib.pyplot as plt

# import matplotlib

def install(package):

subprocess.call([sys.executable, “-m”, “pip”, “install”, package])

packagesInstalled = False

if sys.version_info[0] < 3:

raise Exception(“\nYou are using a deprecated version of Python. Visit the Python website to update to Python 3.\n”)

try:

import numpy as np

from scipy.integrate import odeint

except ImportError:

print(“\nYou are missing Python packages necessary to run this file. This installation will only occur once.\n”)

packagesInstalled = True

install(“scipy”)

import numpy as np

from scipy.integrate import odeint

try:

import matplotlib.pyplot as plt

import matplotlib

except ImportError:

if not packagesInstalled:

print(“\nYou are missing Python packages necessary to run this file. This installation will only occur once.\n”)

install(“matplotlib”)

import matplotlib.pyplot as plt

import matplotlib

# —– Start of differential equation solver —– #

# declare constants

k1 = 0.45

k2 = 0.05

# initial conditions

cA0 = 10

cB0 = 0

# returns a 2D array, [cA'(t), cB'(t)]. This needs to be a function because

# the first argument of the proceeding ODE integrator must be a callable function.

def slope(y, t, k1, k2):

cA, cB = y

dydt = [-k1 * cA, k1 * cA – k2 * cB ** 2]

return dydt

# initial time

t0 = 0

# final time

tf = 60

# 1000 numbers equally spaced between t0 and tf

t = np.linspace(t0, tf, 1000)

# initial conditions

y0 = [cA0, cB0]

# odeint is an ordinary differential equation solver, part of the scipy library. See documentation at

# docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html

sol = odeint(slope, y0, t, args=(k1, k2))

# update font size on the plot

matplotlib.rcParams.update({‘font.size’: 22, ‘font.weight’: ‘normal’})

# this plot will be 12 inches wide, 8 inches high. Actual size may vary.

plt.figure(figsize=(12, 8))

# adds cA and cB to the plot in blue (‘b’) and green (‘g’)

plt.plot(t, sol[:, 0], ‘b’, label=’cA(t)’)

plt.plot(t, sol[:, 1], ‘g’, label=’cB(t)’)

# axis labels

plt.xlabel(‘t’)

plt.ylabel(‘concentration (mol/L)’)

# adds a grid, and finally, displays the plot in a new window.

plt.grid()

plt.show()
