import sympy as sp
from sympy.abc import x

def build_poly_exp_from_coeffs(coeffs, degree):
    exp = 0
    for i in range(degree+1):
        exp+=coeffs[i]*(x**(degree-i))
    return exp

def build_poly_exp_from_roots(roots):
    exp = 1
    for r in roots:
        exp = exp*(x - r)
    exp = sp.expand(exp)
    return exp

def get_coeffs_from_roots(roots):
    exp = build_poly_exp_from_roots(roots)
    print(exp)
    poly = sp.Poly(exp, x)
    coeffs = [int(c) for c in poly.all_coeffs()]
    return coeffs
    