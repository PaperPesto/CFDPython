import numpy
from matplotlib import pyplot
import time
import sys

nx = 41  # try changing this number from 41 to 81 and Run All ... what happens?
dx = 2 / (nx-1)
nt = 25  # nt is the number of timesteps we want to calculate
dt = .025  # dt is the amount of time each timestep covers (delta t)
c = 1  # assume wavespeed of c = 1

u = numpy.ones(nx)  # numpy function ones()
# setting u = 2 between 0.5 and 1 as per our I.C.s
u[int(.5 / dx):int(1 / dx + 1)] = 2
print(u)

pyplot.figure()
pyplot.plot(numpy.linspace(0, 2, nx), u)

# pyplot.show()


un = numpy.ones(nx)  # initialize a temporary array

for n in range(nt):  # loop for values of n from 0 to nt, so it will run nt times
    un = u.copy()  # copy the existing values of u into un
    for i in range(1, nx):  # you can try commenting this line and...
        # for i in range(nx): ## ... uncommenting this line and see what happens!
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])

pyplot.figure()
pyplot.plot(numpy.linspace(0, 2, nx), u)

pyplot.show()
