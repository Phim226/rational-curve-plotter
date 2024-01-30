from curve.random_polynomial import RandPolynomial
from curve.rational_function import RationalFunction
from curve.rational_function import RationalDerivative

def initialise_random_polynomials(num_degree = None, den_degree = None):
    return [RandPolynomial(num_degree), RandPolynomial(den_degree)]

def initialise_curve_objects(**forced_values):
    global numerator, denominator, rational_function, derivative
    force_num_degree, force_den_degree = forced_values.get('forced')[0], forced_values.get('forced')[1]
    forced_num_degree, forced_den_degree = forced_values.get('forced_degrees')[0], forced_values.get('forced_degrees')[1]
    if force_num_degree and not force_den_degree:
        numerator, denominator = initialise_random_polynomials(num_degree = forced_num_degree)
    elif not force_num_degree and force_den_degree:
        numerator, denominator = initialise_random_polynomials(den_degree = forced_den_degree)
    elif force_num_degree and force_den_degree:
        numerator, denominator = initialise_random_polynomials(num_degree = forced_num_degree, den_degree = forced_den_degree)
    else:
        numerator, denominator = initialise_random_polynomials()
    #change these coefficients to manually assign coefficients for debugging
    #numerator = RandPolynomial(coefficients=[-10, -2, -4])
    #denominator = RandPolynomial(coefficients=[-2,0,0])
    print("numerator coefficients: ", numerator.coefficients)
    print("denominator coefficients: ", denominator.coefficients)
    rational_function = RationalFunction(numerator, denominator)
    derivative = RationalDerivative(numerator, denominator)