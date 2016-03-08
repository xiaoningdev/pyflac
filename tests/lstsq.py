# -*- coding: utf-8 -*-
"""
   Example of lstsq.

   Author: Xiaoning Zhang

   @copyright: (c) 2016 by Xiaoning Zhang (xiaoningdev@gmail.com).
   @license: GPL(GNU General Public License).
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
A = np.vstack([x, np.ones(len(x))]).T
print "A:", A
print "y:", y
m, c = np.linalg.lstsq(A, y)[0]
print m, c
print np.linalg.lstsq(A, y)

# plt.plot(x, y, 'o', label='Original data', markersize=10)
# plt.plot(x, m*x + c, 'r', label='Fitted line')
# plt.legend()
# plt.show()
