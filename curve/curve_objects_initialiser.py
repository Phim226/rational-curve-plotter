from curve.random_polynomial import RandPolynomial
from curve.rational_function import RationalFunction
from main_window.element_keys import *
import sympy as sp

def _initialise_random_polynomials(num_degree = None, den_degree = None):
    return [RandPolynomial(num_degree), RandPolynomial(den_degree)]

def initialise_curve_objects(values) -> None:
    global numerator, denominator, rational_function
    force_num_degree, force_den_degree = values[RANDOM_FORCE_NUM_DEG_KEY], values[RANDOM_FORCE_DEN_DEG_KEY]
    forced_num_degree, forced_den_degree = values[RANDOM_NUM_DEG_SPIN_KEY], values[RANDOM_DEN_DEG_SPIN_KEY]
    if force_num_degree and not force_den_degree:
        numerator, denominator = _initialise_random_polynomials(num_degree = forced_num_degree)
    elif not force_num_degree and force_den_degree:
        numerator, denominator = _initialise_random_polynomials(den_degree = forced_den_degree)
    elif force_num_degree and force_den_degree:
        numerator, denominator = _initialise_random_polynomials(num_degree = forced_num_degree, den_degree = forced_den_degree)
    else:
        numerator, denominator = _initialise_random_polynomials()
    #change these coefficients to manually assign coefficients for debugging
    #numerator = RandPolynomial(forced_degree = None, coefficients=[10, 3, -3])
    #denominator = RandPolynomial(forced_degree= None, coefficients=[-9,5,-5])
    print("numerator coefficients: ", numerator.coefficients)
    print("denominator coefficients: ", denominator.coefficients)
    rational_function = RationalFunction(numerator, denominator)