import numpy as np

v_0x = [1.08, 0.9802, 1.06, 1.18, 1.26, 1.20, 1.29, 1.30, 1.23, 1.26]
v_0y = [1.98, 1.94, 1.72, 2.08, 2.08, 1.76, 1.80, 2.08, 1.82, 1.91]

vx_avg = np.average(v_0x)
vy_avg = np.average(v_0y)



def standardavviket(målinger):
    N = len(målinger)
    avg = np.average(målinger)
    delta = 0
    for måling in målinger:
        delta += (1/(N-1))*(måling - avg)**2
    delta = np.sqrt(delta)
    return delta


print("v_0x =",round(vx_avg,2),  "+/-", round(standardavviket(v_0x),2))

print()

print("v_0y =",round(vy_avg,2),  "+/-", round(standardavviket(v_0y),2))
