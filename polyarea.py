def polygon(x, y):
    """
    Calculate the area of a polygon given its x and y coordinates.
    """
    n = len(x)
    A = 0
    for i in range(n):
        A += x[i] * y[(i+1) %n] # the modluo indicates the xn*y1
        A -= x[(i+1)%n] * y[i]
    return abs(A) / 2

def test_triang():
    x = [0, 1, 0]
    y = [0, 0, 1]
    Area = polygon(x, y)
    A_exact = 0.5
    Error = abs(Area - A_exact)
    print("Triangle Test")
    print(f"Exact Area: {A_exact:.2f}")
    print(f"Numerical Area: {Area:.2f}")
    print(f"The error is {Error:.10f}\n")

def test_quad():
    x = [0, 1, 1, 0]
    y = [0, 0, 1, 1]
    Area = polygon(x, y)
    A_exact = 1.0
    Error = abs(Area - A_exact)
    print("Quadrilateral Test")
    print(f"Exact Area: {A_exact:.2f}")
    print(f"Numerical Area: {Area:.2f}")
    print(f"The error is {Error:.10f}\n")

def test_pent():
    x = [0, 1, 2, 2, 0]
    y = [0, 0, 1, 2, 1]
    Area = polygon(x, y)
    A_exact = 2.5
    Error = abs(Area - A_exact)
    print("Pentagon Test")
    print(f"Exact Area: {A_exact:.2f}")
    print(f"Numerical Area: {Area:.2f}")
    print(f"The error is {Error:.10f}\n")

if __name__ == "__main__":
    test_triang()
    test_quad()
    test_pent()
