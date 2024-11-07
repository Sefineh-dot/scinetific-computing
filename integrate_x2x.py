from trapezoidal_t import trapezoidal
from midpoint import midpoint

def adaptive_integration(f, a, b, eps, method='midpoint'):
    n_limit = 100000  # To avoid infinite while loop
    n = 2
    
    if method == 'trapezoidal':
        integral_n = trapezoidal(f, a, b, n)
        integral_2n = trapezoidal(f, a, b, 2 * n)
        diff = abs(integral_2n - integral_n)
        print(f"trapezoidal diff: {diff:g}")
        n *= 2
        
        while (diff > eps) and (n < n_limit):
            integral_n = trapezoidal(f, a, b, n)
            integral_2n = trapezoidal(f, a, b, 2 * n)
            diff = abs(integral_2n - integral_n)
            print(f"trapezoidal diff: {diff:g}")
            n *= 2
            
    elif method == 'midpoint':
        integral_n = midpoint(f, a, b, n)
        integral_2n = midpoint(f, a, b, 2 * n)
        diff = abs(integral_2n - integral_n)
        print(f"midpoint diff: {diff:g}")
        
        while (diff > eps) and (n < n_limit):
            integral_n = midpoint(f, a, b, n)
            integral_2n = midpoint(f, a, b, 2 * n)
            diff = abs(integral_2n - integral_n)
            print(f"midpoint diff: {diff:g}")
            n *= 2
            
    else:
        print('Error - adaptive integration called with unknown parameter')
        return None

    if diff <= eps:
        print(f"The integral computes to: {integral_2n:g}")
        return integral_2n 
    else:
        print("Integration did not converge within the limit.")
        return None  # Integration did not find a solution within limits

def integrate_x2x(a, b, eps):
    def f(x):
        return x**x

    # Choose the integration method ('trapezoidal' or 'midpoint')
    method = 'trapezoidal'

    # Perform the integration using the adaptive integration method
    result = adaptive_integration(f, a, b, eps, method)
    return result

def app():
    a = 0.001  
    b = 4
    eps = 1e-5

    # Perform integration
    result = integrate_x2x(a, b, eps)
    if result is not None:
        print(f"The integration of x^x from {a} to {b} is approximately: {result:.4f}")
    else:
        print("Integration failed to converge.")

if __name__ == "__main__":
    app()
