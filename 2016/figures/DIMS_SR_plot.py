#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("ticks", rc={'font.family': 'Helvetica'})
sns.set_context("paper")

x = np.linspace(-10**-3,10**-3,100)

def fun1(x):
    if x > 0:
        return np.exp(-np.square(np.absolute(x/10**-4)))
    else:
        return 1

def fun2(x):
    if x > 0:
        return np.exp(-np.square(np.absolute(x/30**-4)))
    else:
        return 1

def fun3(x):
    if x > 0:
        return np.exp(-np.square(np.absolute(x/50**-4)))
    else:
        return 1

vfun1 = np.vectorize(fun1)
vfun2 = np.vectorize(fun2)
vfun3 = np.vectorize(fun3)

y1 = vfun1
#y2 = vfun2(x)
#y3 = vfun3(x)

plt.plot(x,y1)
#plt.plot(x,y2)
#plt.plot(x,y3)
plt.show()
