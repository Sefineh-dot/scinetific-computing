import numpy as np
import matplotlib.pyplot as plt

# Differential equation function
def f(t, y):
    return -y + t * y**3

# Newton's method for solving nonlinear equations
def Newton(g, dg, y_guess, tol=1e-6, max_iter=100):
    y_next = y_guess
    for _ in range(max_iter):
        y_new = y_next - g(y_next) / dg(y_next)
        if abs(y_new - y_next) < tol:
            return y_new
        y_next = y_new
    raise RuntimeError("Newton's method did not converge")

# Forward Euler method
def nonlinFE(f, y0, t0, t_end, dt):
    t = np.arange(t0, t_end + dt, dt)
    y = np.zeros_like(t)
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + dt * f(t[i-1], y[i-1])
    return t, y

# Backward Euler method with Newton's method
def nonlinBE(f, y0, t0, t_end, dt):
    t = np.arange(t0, t_end + dt, dt)
    y = np.zeros_like(t)
    y[0] = y0
    for i in range(1, len(t)):
        t_next = t[i]
        y_prev = y[i-1]
        # Implicit function for Newton's method
        g = lambda y_next: y_next - y_prev - dt * f(t_next, y_next)
        dg = lambda y_next: 1 - dt * (-1 + 3 * t_next * y_next**2)  # derivative of g with respect to y_next
        # Initial guess for Newton's method
        y_guess = y_prev
        y[i] = Newton(g, dg, y_guess)
    return t, y

# Actual solution from Wolfram Alpha
def actual_solution(t):
    return np.sqrt(2) / np.sqrt(7 * np.exp(2 * t) + 2 * t + 1)

# Parameters
y0 = 0.5
t0 = 0.0
t_end = 4.0
dt = 0.1

# Numerical solutions
t_fe, y_fe = nonlinFE(f, y0, t0, t_end, dt)
t_be, y_be = nonlinBE(f, y0, t0, t_end, dt)

# Actual solution
t_actual = np.linspace(t0, t_end, 1000)
y_actual = actual_solution(t_actual)

# Plotting
plt.plot(t_fe, y_fe, 'b', label='NonlinFE (Forward Euler)')
plt.plot(t_be, y_be, 'r--', label='NonlinBE (Backward Euler)')
plt.plot(t_actual, y_actual, 'g', label='Actual Solution')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Comparison of Euler Methods with Actual Solution')
plt.legend()
plt.grid(True)
plt.show()
