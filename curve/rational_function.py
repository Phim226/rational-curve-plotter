from sympy.abc import x
import sympy as sp
import numpy as np
import curve.symbol_handler as sh

#TODO: (MAYBE) generate properly formatted derivative function to display in analytics section
class RationalFunction():

     def __init__(self, numerator, denominator):
         self.numerator = numerator
         self.denominator = denominator
         self.rational_expression = numerator.symbolic_expression/denominator.symbolic_expression
         self.der_expression = sp.diff(self.rational_expression, x)
         self.second_der_expression = sp.diff(self.der_expression, x)
         self.function_latex = sh.format_rat_func_label(self.numerator, self.denominator)
         self.function_evaluator = sp.lambdify(x, self.rational_expression, "numpy") #"numpy" argument gives lambdify function access to numpy functions backed by compiled C code, which makes execution faster (without ~1microsecond, with~10nanoseconds)
         self.der_evaluator = sp.lambdify(x, self.der_expression, "numpy")
         self.second_der_evaluator = sp.lambdify(x, self.second_der_expression, "numpy")
         self.discontinuities = self._find_discontinuities(numerator.symbolic_expression, denominator.symbolic_expression)
         self.reduces_to_constant = self.check_if_function_reduces_to_constant(self.rational_expression)

     def _find_discontinuities(self, numerator_expression, denominator_expression):
          inverted_rational_exp = denominator_expression/numerator_expression
          poles = sp.solve(inverted_rational_exp, x)
          discontinuities = []
          for r in poles:
               if r.is_real:
                   discontinuities.append(float(r))
          return sorted(discontinuities)

     #returns True if numerator and denominator cancel each other out and the function reduces to a constant
     def check_if_function_reduces_to_constant(self, expression): 
         return sp.simplify(expression).is_real

     def calculate_y_intercept(self):
          for d in self.discontinuities:
               if np.isclose(d, 0):
                    return None
          return self.function_evaluator(0)

     def calculate_roots(self, show_complex_roots=False):
          roots = sp.solve(self.rational_expression, x)
          if show_complex_roots:
               return roots
          real_roots =[]
          for r in roots:
               if r.is_real:
                    real_roots.append(r)
          return real_roots
          
     
     #TODO: include logic for handling when stationary/inflection points are "nice" i.e integers or rationals so they can be listed "nicely"
     def _calculate_nth_der_stationary_points(self, nth_der_expression, decimal_places = None):
          stat_points = []
          num_stat_points = 0
          for p in sp.solve(nth_der_expression, x):
               print(p)
               p_eval = p.evalf()
               if np.isclose(float(sp.im(p_eval)), 0):
                    stat_points.append((round(sp.re(p_eval), decimal_places), round(sp.re(self.function_evaluator(p_eval)), decimal_places)))
                    num_stat_points+=1
          return [stat_points, num_stat_points]

     def calculate_stationary_points(self, decimal_places = 3):
          stat_points, num_stat_points = self._calculate_nth_der_stationary_points(self.der_expression, decimal_places)
          print("There are " + str(num_stat_points) + " stationary points")
          print("Stationary points are: ", stat_points)
          return stat_points
     
     def calculate_inflection_points(self, decimal_places = 3):
          inflec_points, num_inflec_points = self._calculate_nth_der_stationary_points(self.second_der_expression, decimal_places)
          print("There are " + str(num_inflec_points) + " inflection points")
          print("Inflection points are: ", inflec_points)
          return inflec_points
     
     def calculate_derivative_coefficients(self, num_coeffs, den_coeffs):
         der_num_coeffs = np.polysub(np.polymul(np.polyder(num_coeffs), den_coeffs), np.polymul(np.polyder(den_coeffs), num_coeffs))
         der_den_coeffs = np.polymul(den_coeffs, den_coeffs)
         return [der_num_coeffs, der_den_coeffs]

    

