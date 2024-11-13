import numpy as np
import matplotlib.pyplot as plt

def fixed_point_iteration(f, x0, tol, max_iter=100):

   # This function finds the fixed point of a function using the fixed-point iteration method.
    x = x0
    for i in range(max_iter):
        x_new = f(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Failed to converge within the maximum iterations")

def app():
    f = lambda x: (np.exp(-x) - x**3) / 2
    x0 = 1
    tol = 1e-5

    # Perform fixed-point iteration
    try:
        root = fixed_point_iteration(f, x0, tol)
        print(f"The solution for the given function is approximately: {root:.4f}")
    except ValueError as e:
        print(e)

    # Plot the function and the line y = x for visualization
    x_values = np.linspace(-2, 2, 400)
    y_values = f(x_values)
    y_line = x_values

    plt.plot(x_values, y_values, label='fixed point iteration values')
    plt.plot(x_values, y_line, label='$y = x$', linestyle='--')
    plt.axhline(0, color='gray', linestyle='--')  # Horizontal line at y=0
    plt.axvline(0, color='gray', linestyle='--')  # Vertical line at x=0
    plt.title('Fixed-Point Iteration Function and y=x Line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    app()
