from curve.random_polynomial import RandPolynomial
from curve.rational_function import RationalFunction
from main_window.element_keys import *
import sympy as sp

def initialise_curve_objects(values) -> None:
    global numerator, denominator, rational_function
    force_num_degree, force_den_degree = values[RANDOM_FORCE_NUM_DEG_KEY], values[RANDOM_FORCE_DEN_DEG_KEY]
    max_num_degree, max_den_degree = values[RANDOM_NUM_DEG_SPIN_KEY], values[RANDOM_DEN_DEG_SPIN_KEY]
    numerator, denominator = RandPolynomial(max_num_degree, force_num_degree), RandPolynomial(max_den_degree, force_den_degree)
    #change these coefficients to manually assign coefficients for debugging
    #numerator = RandPolynomial(coefficients=[-6,10, -7])
    #denominator = RandPolynomial(coefficients=[9,-5,-3,7])
    print("numerator coefficients: ", numerator.coefficients)
    print("denominator coefficients: ", denominator.coefficients)
    rational_function = RationalFunction(numerator, denominator)