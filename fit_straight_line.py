import matplotlib.pyplot as plt

def calcError(x, y, a, b):
    e = 0  # Initialize the error
    for i in range(len(x)):  # Loop through all elements
        e += (a * x[i] + b - y[i]) ** 2  # Find the square and sum the error for the entire loop
    return e  # Return the error

def fit_straight_line():
    x = [0, 1, 2, 3, 4]
    y = [0.5, 2.0, 1.0, 1.5, 7.5]

    while True:
        try:
            a = float(input("a: "))
            b = float(input("b: "))
    
            # Calculate error
            error = calcError(x, y, a, b)
            print(f"The error is: {error:.2f}")
    
            # Generate line values for plotting
            y_line = [a * xi + b for xi in x]
    
            # Plot the measurements and the line
            plt.figure(figsize=(8, 6))
            plt.plot(x, y_line, 'b-', label=f'f(x) = {a}x + {b}')
            plt.scatter(x, y, color='red', label='Measurements')
            plt.xlabel('time')
            plt.ylabel('y')
            plt.legend()
            plt.title('Line Fit and Measurements')
            plt.grid(True)
            plt.show()
            
            # for other try
            redo = input("Enter other a and b? (yes/no): ")
            if redo.lower() != 'yes':
                break
                
        except ValueError:
            print("Invalid input")
            continue

# Test the function 
if __name__ == "__main__":
    fit_straight_line()
