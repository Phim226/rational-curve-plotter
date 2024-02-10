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

def format_rat_func_label(numerator, denominator):
    numerator_exp = build_poly_exp_from_coeffs(numerator.coefficients, numerator.degree) 
    denominator_exp = build_poly_exp_from_coeffs(denominator.coefficients, denominator.degree)
    rat_func_exp = numerator_exp/denominator_exp
    return sp.latex(rat_func_exp)

def get_coeffs_from_roots(roots):
    exp = build_poly_exp_from_roots(roots)
    print(exp)
    poly = sp.Poly(exp, x)
    coeffs = poly.all_coeffs()
    return coeffs
    