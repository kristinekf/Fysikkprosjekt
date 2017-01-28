import numpy as np
import math
import matplotlib.pyplot as plt

m = 0.1  # mass of particle, kg
g = 9.81 # tyngdeakselerasjonen, m/s^2

N = 100000  # number of steps
h = 0.001  # step size

# initial values
t_0 = 0.0
v_0 = 5.0 # utgangshastighet, m/s
theta = 45 # utgangsvinkel, grader
v_x0 = v_0 * math.cos(math.radians(theta))  # x-hastighet ved start
v_y0 = v_0 * math.sin(math.radians(theta))  # y-hastighet ved start
s_x0 = 0.0  # startposisjon, meter
s_y0 = 0.0  # startposisjon, meter

print("Masse:",m, "kg")
print("Startfart:",v_0, "m/s")
print("Utgangsvinkel:",theta, "grader")
print("Startposisjon: (", s_x0, ", ", s_y0, ")", sep="")
print()


# Without air resistance:

D = 0  # drag coefficient

t = np.zeros(N + 1)
vx = np.zeros(N + 1)
vy = np.zeros(N + 1)
sx = np.zeros(N + 1)
sy = np.zeros(N + 1)

t[0] = t_0
vx[0] = v_x0
sx[0] = s_x0
vy[0] = v_y0
sy[0] = s_y0

for n in range(N):
    # Euler's method
    sx_new = sx[n] + h*vx[n]
    vx_new = vx[n] + h * (- (D / m) * math.sqrt(vx[n]**2 + vy[n]**2) * vx[n])

    sy_new = sy[n] + h * vy[n]
    vy_new = vy[n] + h * (-g - (D / m) * math.sqrt(vx[n]**2 + vy[n]**2) * vy[n])

    t[n + 1] = t[n] + h
    vx[n + 1] = vx_new
    sx[n + 1] = sx_new

    vy[n + 1] = vy_new
    sy[n + 1] = sy_new

    if sy[n+1] < 0:
        print("Luftmotstandskonstant = ", D,":", sep="")
        print("Legemet lander etter ca.", round(t[n-1], 2), "sekunder.")
        print("Legemet lander ca.", round(sx[n-1], 2), "meter unna startposisjonen.")
        print()
        break

# With air resistance:

D = 0.01  # drag coefficient

t2 = np.zeros(N + 1)
vx2 = np.zeros(N + 1)
vy2 = np.zeros(N + 1)
sx2 = np.zeros(N + 1)
sy2 = np.zeros(N + 1)

t2[0] = t_0
vx2[0] = v_x0
sx2[0] = s_x0
vy2[0] = v_y0
sy2[0] = s_y0

for n in range(N):
    # Euler's method
    sx_new2 = sx2[n] + h*vx2[n]
    vx_new2 = vx2[n] + h * (- (D / m) * math.sqrt(vx2[n]**2 + vy2[n]**2) * vx2[n])

    sy_new2 = sy2[n] + h * vy2[n]
    vy_new2 = vy2[n] + h * (-g - (D / m) * math.sqrt(vx2[n]**2 + vy2[n]**2) * vy2[n])

    t2[n + 1] = t2[n] + h
    vx2[n + 1] = vx_new2
    sx2[n + 1] = sx_new2

    vy2[n + 1] = vy_new2
    sy2[n + 1] = sy_new2

    if sy2[n+1] < 0:
        print("Luftmotstandskonstant = ", D, ":", sep="")
        print("Legemet lander etter ca.", round(t2[n-1], 2), "sekunder.")
        print("Legemet lander ca.", round(sx2[n-1], 2), "meter unna startposisjonen.")
        print()
        break


plt.figure()
plt.plot(sx,sy,sx2,sy2)
plt.xlabel(r'$s_x$')
plt.ylabel(r'$s_y$')
plt.grid()

#plt.figure()
#plt.plot(sx2,sy2)
#plt.xlabel(r'$s2_x$')
#plt.ylabel(r'$s2_y$')
#plt.grid()

plt.show()

