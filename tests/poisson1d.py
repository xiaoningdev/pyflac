# -*- coding: utf-8 -*-
"""
   Example of poisson 1D.

   Solution of 1D Poisson equation d2FI/dx2=1
   with finite differences on a regular grid
   using direct solver '\'

   Author: Xiaoning Zhang

   @copyright: (c) 2016 by Xiaoning Zhang (xiaoningdev@gmail.com).
   @license: GPL(GNU General Public License).
"""

import numpy as np
from scipy import sparse, linalg
import matplotlib.pyplot as plt


# Numerical model parameters
xsize = 1000000  # Model size, m
xnum = 1000     # Number of nodes
xstp = xsize/(xnum-1)  # Grid step
print "xstp =>", xstp

# Right part of Poisson equation is = 1
# Boundary conditions: FI=0

# Matrix of coefficients initialization
L = sparse.csr_matrix((xnum, xnum))
# Vector of right part initialization
R = np.zeros((xnum, 1))

# Composing matrix of coefficients L()
# and vector (column) of right parts R()
# First point: FI=0
L[0, 0] = 1
R[0, 0] = 0

# Intermediate points
for i in range(2, xnum - 1):
    # d2FI/dx2=1
    # (FI(i-1)-2*FI(i)+FI(i+1))/dx^2=1
    L[i, i-1] = 1 / (xstp*xstp)
    L[i, i] = -2 / (xstp*xstp)
    L[i, i+1] = 1 / (xstp*xstp)
    R[i, 0] = 1

# Last point: FI=0
L[xnum-1, xnum-1] = 1
R[xnum-1, 0] = 0

# Obtaining vector (line) of solutions FI()
try:
    FI = linalg.solve(L.toarray(), R)
except Exception as e:
    FI = linalg.lstsq(L.toarray(), R)

#Create vector for nodal point positions
x = range(0, xsize, xstp)
x = [xx / 1000 for xx in x]

# Plot the solution
fig, ax = plt.subplots()
ax.plot(x, FI[0], 'go-', label='gravity potential', linewidth=2)

# add some
ax.set_xlabel('x, km')
ax.set_ylabel('gravity potential, J/kg')
ax.set_title('Solution of 1D Poisson equation')

minx = min(x)
maxx = max(x)
gap = (maxx - minx) * 0.1

ax.axis([minx-gap, maxx+gap, min(FI[0])-1, max(FI[0])+1])
ax.legend()

plt.show()
