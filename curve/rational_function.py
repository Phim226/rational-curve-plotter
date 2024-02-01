import numpy as np
import sympy as sp
import curve.symbol_handler as sh

#TODO: (MAYBE) generate properly formatted derivative function to display in analytics section


class RationalFunction():

     x = sp.symbols('x')

     def __init__(self, numerator, denominator):
         self.numerator = numerator
         self.denominator = denominator
         self.rational_expression = numerator.symbolic_expression/denominator.symbolic_expression
         self.der_expression = sp.diff(self.rational_expression, self.x)
         self.second_der_expression = sp.diff(self.der_expression, self.x)
         self.function_latex = sh.format_rat_func_label(self.numerator, self.denominator)
         self.function_evaluator = sp.lambdify(self.x, self.rational_expression)
         self.der_evaluator = sp.lambdify(self.x, self.der_expression)
         self.second_der_evaluator = sp.lambdify(self.x, self.second_der_expression)
         self.discontinuities = self._find_discontinuities(numerator.symbolic_expression, denominator.symbolic_expression)
         self.reduces_to_constant = self._check_if_rational_func_reduces_to_constant(self.numerator.coefficients, self.denominator.coefficients)

     def _find_discontinuities(self, numerator_expression, denominator_expression):
          inverted_rational_exp = denominator_expression/numerator_expression
          poles = sp.solve(inverted_rational_exp, self.x)
          discontinuities = []
          for r in poles:
               if r.is_real:
                   discontinuities.append(float(r))
          return sorted(discontinuities)

     #returns True if numerator and denominator cancel each other out and the function reduces to a constant
     def _check_if_rational_func_reduces_to_constant(self, num_coeffs, den_coeffs): 
         reduced_func = np.polydiv(num_coeffs, den_coeffs)
         quotient = reduced_func[0]
         remainder = reduced_func[1]
         return ((len(quotient) == 1) and (len(remainder)== 1) and (np.isclose(remainder[0], 0)))

     def calculate_y_intercept(self, reduced_den_roots):
          for r in reduced_den_roots:
               if np.isclose(r, 0):
                    return None
          return self.curve_evaluator(0)

     def calculate_roots(self):
          return sp.solve(self.rational_expression, self.x)
     
     def calculate_stationary_points(self):
          stat_points = []
          num_stat_points = 0
          for p in sp.solve(self.der_expression, self.x):
               if p.is_real:
                    stat_points.append((p, self.function_evaluator(p)))
                    num_stat_points+=1
          print("There are " + str(num_stat_points) + " stationary points")
          return stat_points
     
     def calculate_inflection_points(self):
          inflec_points = []
          num_inflec_points = 0
          for p in sp.solve(self.second_der_expression, self.x):
               if p.is_real:
                    inflec_points.append((p, self.function_evaluator(p)))
                    num_inflec_points+=1
          print("There are " + str(num_inflec_points) + " inflection points")
          return inflec_points
     
     def calculate_derivative_coefficients(self, num_coeffs, den_coeffs):
         der_num_coeffs = np.polysub(np.polymul(np.polyder(num_coeffs), den_coeffs), np.polymul(np.polyder(den_coeffs), num_coeffs))
         der_den_coeffs = np.polymul(den_coeffs, den_coeffs)
         return [der_num_coeffs, der_den_coeffs]

    

