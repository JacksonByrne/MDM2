import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ---- PARAMETERS ----
k = 1.0  # permeability-like constant (example)
m = 1.0  # mass or similar parameter
theta_deg = 20  # angle in degrees
# convert to radians for numpy trig functions
theta = np.deg2rad(theta_deg)
x = 0.5  # thickness (unused placeholder)

# ---- BOUNDARIES ----
# avoid L=0 because area A(L)=0 at L=0 would cause division-by-zero in some expressions
L_span = [1e-6, 1.0]
Qout = 1.0  # GUESS to match Qin
y0 = [0.0, Qout]


def R(L):
    """Radius as a function of L using angle in radians."""
    return np.tan(theta) * L


def dRdL(L):
    return np.tan(theta)


def A(L):
    return np.pi * R(L) ** 2


def dAdL(L):
    return np.pi * 2 * R(L) * dRdL(L)

for L in range(1):
    for P in range(0, 5):
        b = -1/(k*m) * dAdL(L) * P
        print (b)

def system(L, y):
    """Coupled ODE system: y = [P, Q]"""
    P, Q = y
    # protect against A(L)==0 (shouldn't happen because L_span starts >0)
    aL = A(L)
    if aL == 0:
        dP_dL = 0.0
    else:
        dP_dL = -1.0 / (k * aL) * Q
    dQ_dL = -1.0 / (k * m) * dAdL(L) * P
    return [dP_dL, dQ_dL]


def run_mdm2_demo():
    """Solve the ODE over L_span and plot P(L) and Q(L)."""
    try:
        sol = solve_ivp(system, L_span, y0, method='Radau', dense_output=False)
    except Exception as e:
        print('ODE solve failed:', e)
        return

    if not sol.success:
        print('Solver failed:', sol.message)
        return

    print('ODE solver success. t_span:', sol.t_min, '->', sol.t_max)
    plt.plot(sol.t, sol.y[0], label='P(L)')
    plt.plot(sol.t, sol.y[1], label='Q(L)')
    plt.xlabel('L')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Solutions of Coupled ODEs')
    plt.show()


if __name__ == '__main__':
    run_mdm2_demo()
