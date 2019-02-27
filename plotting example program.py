# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:28:32 2019

@author: mvanstav
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,.1)

# Most useful plotting function: Just plain old plot(). Here's how it works.
# The next few lines show creating different figures and plotting things
# Notice the effect of giving plot two arrays versus one (what's the x axis then?)
# ALso see how I can pop back and forth between plots
plt.figure(1)
plt.plot(x,x**2)

plt.figure(2)
plt.plot(x**3)

plt.figure(1)
plt.plot(x**2)
plt.xlim(0,20) # rescale the x axis

# I prefer to have figures pop up in separate windows rather than the console
# so that I can interact with them. To do that, Tools->Preferences->Ipython console
# -> Graphics and switch the backend to "automatic"
# then you can do things like type the following into the console:
#plt.figure(1)
#plt.ylim(0,50)
# and it'll zoom the figure for you
# If either of you figure out how to do that sort of thing on figures in the
# console, let me know
# Oh the figures will pop up in the background. They just do that.

# There are a million parameters you can change. Learn them as you go.

#Next up: image plots. First, let me make a nice array

X,Y=np.meshgrid(x,x) #this is a clever function

print(np.shape(X)) #printing shapes so you can see what's happening here
print(np.shape(Y))

#the next two figures show you contours of the X and Y coordinate arrays created above
plt.figure(3)
plt.clf() #good habit to clear a figure before you use it again
plt.contour(X)

plt.figure(4)
plt.clf()
plt.contourf(Y)

#now I'll make a data array that has some features we might want to look at in an image plot
imagearray=np.exp(-(X-5)**2-.2*(Y-2)**2) +.01*np.exp(-(X-8)**2-2**(Y-8)**2)#two gaussians in 2D

#and here I plot my sample data, throwing a colorbar on it to show the scale
plt.figure(5)
plt.clf()
plt.imshow(imagearray)
plt.colorbar()

#after you run the program, type the following line in the console to see the second gaussian
#plt.clim(0,.01)