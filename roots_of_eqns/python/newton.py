#module newton
''' root = NewtonRaphson(f, df, a, b, tol=1.0e-9, maxiter=30).
Finds a root of f(x) in (a, b) by combining
Bisection method and Newton-Raphson method.
the functions f and its derivative df have
to be definded by the user.
'''
from numpy import sign

def NewtonRaphson(f, df, a, b, tol=1.0e-9, maxiter=30):

    fa = f(a)
    if fa ==0: return a
    fb = f(b)
    if fb == 0: return b

    if sign(fa) == sign(fb): print('Roots are not bracketed!'); exit
    x = 0.5 * (a + b)
    for i in range(maxiter):
        fx = f(x)
        if fx ==0.0: return x

        # Tighten the brackets
        if sign(fa) != sign(fx): b = x
        else: a = x

        # Try a Newton-Raphson step
        dfx = df(x)
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx

        # If result is outside the bracket, use Bisection
        if (b - x) * (x - a) < 0.0:
            dx = 0.5 * (b - a)
            x = a + dx

        # Check for convergence
        if abs(dx) < tol*max(abs(b), 1.0): return x

    print('Too many iterations in Newton-Raphson')
