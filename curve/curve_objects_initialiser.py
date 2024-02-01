from curve.random_polynomial import RandPolynomial
from curve.rational_function import RationalFunction
from main_window.element_keys import *

def initialise_random_polynomials(num_degree = None, den_degree = None):
    return [RandPolynomial(num_degree), RandPolynomial(den_degree)]

def initialise_curve_objects(values):
    global numerator, denominator, rational_function
    force_num_degree, force_den_degree = values[FORCE_NUM_DEG_KEY], values[FORCE_DEN_DEG_KEY]
    forced_num_degree, forced_den_degree = values[NUM_DEG_SPIN_KEY], values[DEN_DEG_SPIN_KEY]
    if force_num_degree and not force_den_degree:
        numerator, denominator = initialise_random_polynomials(num_degree = forced_num_degree)
    elif not force_num_degree and force_den_degree:
        numerator, denominator = initialise_random_polynomials(den_degree = forced_den_degree)
    elif force_num_degree and force_den_degree:
        numerator, denominator = initialise_random_polynomials(num_degree = forced_num_degree, den_degree = forced_den_degree)
    else:
        numerator, denominator = initialise_random_polynomials()
    #change these coefficients to manually assign coefficients for debugging
    #numerator = RandPolynomial(coefficients=[5,-3,6])
    #denominator = RandPolynomial(coefficients=[4,6,6])
    print("numerator coefficients: ", numerator.coefficients)
    print("denominator coefficients: ", denominator.coefficients)
    rational_function = RationalFunction(numerator, denominator)
    print("stationary points are: ", rational_function.calculate_stationary_points())
    print("inflection points are: ", rational_function.calculate_inflection_points())