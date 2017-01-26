# -*- coding: utf-8 -*-
import numpy as np
import math

m = 0.1  # masse
g = 9.81  # m/s^2
D = 0.0  # luftmotstandkonstant (tilfeldig gjetning)
theta = 30  # utskytningsvinkel, grader
v0 = 5.0  # utgangshastighet, m/s
v0x = v0 * math.cos(math.radians(theta))  # x-hastighet ved start
v0y = v0 * math.sin(math.radians(theta))  # y-hastighet ved start
sx0 = 0.0  # startposisjon, meter
sy0 = 0.0  # startposisjon, meter
h = 0.001  # tidsintervall, delta-t, sekunder
t = 0.0  # tidspunkt t = 0
N = 10000  # iterasjoner

vx = v0x
vy = v0y
sx = sx0
sy = sy0

for i in range(0, N):
    ax = -(D / m) * math.sqrt(vx ** 2 + vy ** 2) * vx
    ay = -g - (D / m) * math.sqrt(vx ** 2 + vy ** 2) * vy

    # plot?

    if sy < 0:
        print("Legemet lander etter ca.", round(t, 2), "sekunder.")
        print("Legemet lander ca.", round(sx, 2), "meter unna startposisjonen.")
        break

    vx = vx + ax * h  # estimat for farten ved enden av tidsintervallet
    vy = vy + ay * h

    sx = sx + vx * h + 0.5 * ax * h ** 2  # estimat for posisjonen ved enden av tidsintervallet
    sy = sy + vy * h + 0.5 * ay * h ** 2

    t = t + h
    

# kodet med hjelp fra http://wps.aw.com/wps/media/objects/877/898586/topics/topic01.pdf