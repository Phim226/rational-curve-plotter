import numpy as np
import sympy as sp
import curve.symbol_handler as sh

#TODO: include function to calculate stationary points 
#TODO: include function to calculate inflection points
#TODO: (MAYBE) generate properly formatted derivative function to display in analytics section


class RationalFunction():

    x = sp.symbols('x')

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduced_denominator_roots = self.reduce_denominator_roots(numerator.symbolic_expression, denominator.symbolic_expression)
        self.reduces_to_constant = self.check_if_rational_func_reduces_to_constant(self.numerator.coefficients, self.denominator.coefficients)

    def reduce_denominator_roots(self, numerator_expression, denominator_expression):
         inverted_rational_exp = denominator_expression/numerator_expression
         roots = sp.solve(inverted_rational_exp, self.x)
         reduced_roots = []
         for r in roots:
              if r.is_real:
                   reduced_roots.append(float(r))
         return reduced_roots


    #returns True if numerator and denominator cancel each other out and the function reduces to a constant
    def check_if_rational_func_reduces_to_constant(self, num_coeffs, den_coeffs): 
        reduced_func = np.polydiv(num_coeffs, den_coeffs)
        quotient = reduced_func[0]
        remainder = reduced_func[1]
        return ((len(quotient) == 1) and (len(remainder)== 1) and (np.isclose(remainder[0], 0)))

    def get_function_evaluator(self, num_coeffs=None, den_coeffs=None):
         if num_coeffs is None and den_coeffs is None:
              return lambda x : (np.polyval(self.numerator.coefficients, x))/(np.polyval(self.denominator.coefficients, x))
         return lambda x : (np.polyval(num_coeffs, x))/(np.polyval(den_coeffs, x))

    def calculate_y_intercept(self, reduced_den_roots):
         for r in reduced_den_roots:
              if np.isclose(r, 0):
                   return None
         return self.curve_evaluator(0)
    
    def format_function_label(self):
         self.function_latex = sh.format_rat_func_label(self.numerator, self.denominator)
         return self.function_latex
    

class RationalDerivative(RationalFunction):
     
    def __init__(self, numerator, denominator):
        super.__init__(self, numerator, denominator)
        num_coeffs, den_coeffs = self.calculate_derivative_coefficients(numerator.coefficients, denominator.coefficients)
        self.function_evaluator = self.get_function_evaluator(num_coeffs, den_coeffs)
    
    def calculate_derivative_coefficients(self, num_coeffs, den_coeffs):
         der_num_coeffs = np.polysub(np.polymul(np.polyder(num_coeffs), den_coeffs), np.polymul(np.polyder(den_coeffs), num_coeffs))
         der_den_coeffs = np.polymul(den_coeffs, den_coeffs)
         return [der_num_coeffs, der_den_coeffs]

