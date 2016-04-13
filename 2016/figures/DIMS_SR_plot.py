#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("ticks", rc={'font.family': 'Helvetica'})
sns.set_context("paper")

def fun (del_phi, phi_0):
    if del_phi > 0:
        return np.exp(-np.square(np.absolute(del_phi/phi_0)))
    else:
        return 1

vfun = np.vectorize(fun)

x = np.linspace(-1e-7,1e-7,100)
y1 = vfun(x,1e-4)
y2 = vfun(x,1e-5)
y3 = vfun(x,1e-6)

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.show()
