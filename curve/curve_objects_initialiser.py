from curve.random_polynomial import RandPolynomial
from curve.rational_function import RationalFunction
from main_window.element_keys import *
import sympy as sp

def initialise_curve_objects(values) -> None:
    global numerator, denominator, rational_function
    force_num_degree, force_den_degree = values[RANDOM_FORCE_NUM_DEG_KEY], values[RANDOM_FORCE_DEN_DEG_KEY]
    max_num_degree, max_den_degree = values[RANDOM_NUM_DEG_SPIN_KEY], values[RANDOM_DEN_DEG_SPIN_KEY]
    random_coefficients = values[RANDOM_COEFFICIENTS_KEY]
    random_roots = values[RANDOM_ROOTS_KEY]
    reduces_to_constant = True
    while reduces_to_constant:
        numerator = RandPolynomial(max_num_degree, force_num_degree, random_coefficients, random_roots)
        denominator = RandPolynomial(max_den_degree, force_den_degree, random_coefficients, random_roots)
        rational_function = RationalFunction(numerator, denominator)
        if not values[EXCLUDE_CONSTANT_KEY]:
            break
        else:
            reduces_to_constant = rational_function.reduces_to_constant
    #change these coefficients to manually assign coefficients for debugging. This bypasses the option to exclude constant curves
    #numerator = RandPolynomial(coefficients=[1,1,1])
    #denominator = RandPolynomial(coefficients=[1,1,1])
    #rational_function = RationalFunction(numerator, denominator)
    print("numerator coefficients: ", numerator.coefficients)
    print("denominator coefficients: ", denominator.coefficients)