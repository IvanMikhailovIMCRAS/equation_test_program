import numpy as np

def eq(a: float, b: float, c: float):
    """Solution of equation sqrt(a*x+b)=c respect of x"""
    if c < 0:
        raise Exception("there is no solution")
    elif a == 0 and c != np.sqrt(b):
        raise Exception("there is no solution")
    elif a == 0 and c == np.sqrt(b):
        raise Exception("many solutions")
    else:
        return (c**2 - b) / a
    
if __name__ == '__main__':
    print("Hello!")