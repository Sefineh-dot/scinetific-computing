def interpolate(y, dt, t):
    """
    Interpolates a value at time t using linear interpolation between measurements y taken at intervals dt.
    
    Parameters:
    - y: list or array of measurements (y_i).
    - dt: time interval Δt between consecutive measurements.
    - t: the time at which to interpolate the value.
    
    Returns:
    - Interpolated value at time t.
    """
    i = int(t / dt)
    
    if i < 0 or i >= len(y) - 1:
        raise ValueError("The time t is outside the range of the provided data.")
    
    t_i = i * dt
    interpolated_y = y[i] + (y[i + 1] - y[i]) * (t - t_i) / dt
    
    return interpolated_y

def find_y(y, dt):
   N = (len(y) - 1) * dt  # Maximum time based on the number of measurements

   while True:
        try:
            # Ask the user for a time input
            t = float(input(f"Enter a time between 0 and {N} (or a negative number to quit): "))
            
            # Break the loop if the user enters a negative time
            if t < 0:
                print("Exiting the program.")
                break
            
            # Check if t is within the allowed interval
            if 0 <= t <= N:
                # Calculate and print the interpolated value
                y_interpo = interpolate(y, dt, t)
                print(f"The interpolated value at t = {t} is approximately {y_interpo}")
            else:
                print(f"Time must be within the interval [0, {N}]. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Example for comparison 
y = [4.4, 2.0, 11.0, 21.5, 7.5]  # Measurements y_i
dt = 1  # Time interval Δt between measurements
find_y(y, dt)
