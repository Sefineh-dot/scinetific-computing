import numpy as np
import matplotlib.pyplot as plt

def solve_sir(S_0, I_0, R_0, D, dt, method='euler'):
    beta = 10 / (40 * 8 * 24)
    gamma = 3 / (15 * 24)
    N_t = int(D * 24 / dt)
    t = np.linspace(0, N_t * dt, N_t + 1)
    S, I, R = [np.zeros(N_t + 1) for _ in range(3)]
    S[0], I[0], R[0] = S_0, I_0, R_0
    
    for i in range(N_t):
        if method == 'euler':
            S[i + 1] = S[i] - dt * beta * S[i] * I[i]
            I[i + 1] = I[i] + dt * beta * S[i] * I[i] - dt * gamma * I[i]
            R[i + 1] = R[i] + dt * gamma * I[i]
        else:  # heun
            S_star = S[i] - dt * beta * S[i] * I[i]
            I_star = I[i] + dt * beta * S[i] * I[i] - dt * gamma * I[i]
            R_star = R[i] + dt * gamma * I[i]
            
            S[i + 1] = S[i] - dt * 0.5 * beta * (S[i] * I[i] + S_star * I_star)
            I[i + 1] = I[i] + dt * 0.5 * (beta * S[i] * I[i] - gamma * I[i] + beta * S_star * I_star - gamma * I_star)
            R[i + 1] = R[i] + dt * 0.5 * (gamma * I[i] + gamma * I_star)
    
    return t, S, I, R

# Parameters
D, S_0, I_0, R_0 = 30, 50, 1, 0
dt_large, dt_small = 5.0, 0.1

# Solve for both methods and time steps
results = {
    'large': {
        'euler': solve_sir(S_0, I_0, R_0, D, dt_large, 'euler'),
        'heun': solve_sir(S_0, I_0, R_0, D, dt_large, 'heun')
    },
    'small': {
        'euler': solve_sir(S_0, I_0, R_0, D, dt_small, 'euler'),
        'heun': solve_sir(S_0, I_0, R_0, D, dt_small, 'heun')
    }
}

# Print differences
for step in ['large', 'small']:
    dt = dt_large if step == 'large' else dt_small
    print(f"\nDifferences with {step} time step (dt = {dt}):")
    for i, pop in enumerate(['Susceptible', 'Infected', 'Recovered']):
        diff = np.max(np.abs(results[step]['heun'][i+1] - results[step]['euler'][i+1]))
        print(f"Maximum difference in {pop}: {diff:.6f}")

# Plot results
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
titles = ['Euler Method (Large Time Step)', "Heun's Method (Large Time Step)",
          'Euler Method (Small Time Step)', "Heun's Method (Small Time Step)"]
steps = ['large', 'large', 'small', 'small']
methods = ['euler', 'heun', 'euler', 'heun']

for i, (ax, title, step, method) in enumerate(zip(axs.flat, titles, steps, methods)):
    t, S, I, R = results[step][method]
    ax.plot(t, S, 'b', label='Susceptible')
    ax.plot(t, I, 'r', label='Infected')
    ax.plot(t, R, 'g', label='Recovered')
    ax.set(xlabel='Time (hours)', ylabel='Population', title=title)
    ax.legend()

plt.tight_layout()
plt.show()