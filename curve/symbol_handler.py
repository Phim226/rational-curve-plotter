import sympy as sp

def build_poly_exp(coeffs, degree):
    x = sp.symbols('x')
    exp = 0
    for i in range(degree+1):
        exp+=coeffs[i]*(x**(degree-i))
    return exp

def format_rat_func_label(numerator, denominator):
    numerator_exp = build_poly_exp(numerator.coefficients, numerator.degree) 
    denominator_exp = build_poly_exp(denominator.coefficients, denominator.degree)
    rat_func_exp = numerator_exp/denominator_exp
    return sp.latex(rat_func_exp)