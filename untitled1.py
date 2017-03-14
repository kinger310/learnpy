# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:50:43 2017

@author: Wangdi
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.02)
plt.plot(x, x**2, 'r^', x, x**3, 'bo', x, x, 'y-')
plt.show()
