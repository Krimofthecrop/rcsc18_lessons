import numpy as np

def find_y_on_circle(x):
    """
    The circle equation
    """
    y = np.sqrt(1 - x**2) #circle equation
    return y
    
def est_pi(tot_num):
    """
    This function will estimate pi using the Monte Carlo method in a unit circle.
    """

    inside = 0 
    res = 0 #counter for test points

    while res < tot_num:
        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1)
        if find_y_on_circle(x) >= y: #inside the circle
            inside += 1
        res += 1

    return 4*inside/tot_num #prints pi estimate
