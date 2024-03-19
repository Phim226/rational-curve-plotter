from sympy.abc import x
import sympy as sp
import numpy as np

class RationalFunction():

     def __init__(self, numerator, denominator):
          self.numerator = numerator
          self.denominator = denominator
          self.rational_expression = numerator.symbolic_expression/denominator.symbolic_expression
          self.rational_expression_simp = sp.simplify(self.rational_expression)
          self.der_expression = sp.diff(self.rational_expression, x)
          self.der_expression_as_fraction = self._calculate_der_expression_as_fraction()
          self.second_der_expression = sp.diff(self.der_expression, x)
          self.reduces_to_constant = self._check_if_function_reduces_to_constant(self.rational_expression)
          if self.reduces_to_constant:
               self.function_evaluator = lambda t : (numerator.coefficients[0]*t)/(denominator.coefficients[0]*t)
          elif not self.reduces_to_constant and denominator.symbolic_expression.is_real:
               self.function_evaluator = lambda t : (self._generate_numerator_lambda(numerator.coefficients, t))/(denominator.coefficients[0])
          else:
               self.function_evaluator = sp.lambdify(x, self.rational_expression, "numpy")
          self.der_evaluator = sp.lambdify(x, self.der_expression, "numpy") #"numpy" argument gives lambdify function access to numpy functions backed by compiled C code, which makes execution faster (without ~1microsecond, with~10nanoseconds)
          self.second_der_evaluator = sp.lambdify(x, self.second_der_expression, "numpy")
          exp = self.rational_expression if not denominator.symbolic_expression.is_Rational and not denominator.symbolic_expression.is_Add else self.rational_expression_simp
          self.discontinuities = self._find_discontinuities(exp) if not self.reduces_to_constant else []
     
     def _generate_numerator_lambda(self, numerator, t):
          n = 0
          for c in numerator:
               n += c*(t**(len(numerator)-numerator.index(c)-1))
          return n

     def _find_discontinuities(self, rational_expression):
          inverted_rational_exp = sp.simplify(1/rational_expression)
          poles = sp.solve(inverted_rational_exp, x)
          discontinuities = []
          for r in poles:
               if r.is_real:
                   discontinuities.append(float(r))
          return sorted(discontinuities)

     #returns True if numerator and denominator cancel each other out and the function reduces to a constant
     def _check_if_function_reduces_to_constant(self, rational_expression): 
         return sp.simplify(rational_expression).is_real
     
     def _get_point_on_curve(self, x_val, decimal_places, value_is_nice = False):
          if value_is_nice:
               return (sp.re(x_val), sp.re(self.function_evaluator(x_val)))
          return (round(sp.re(x_val), decimal_places), round(sp.re(self.function_evaluator(x_val)), decimal_places))
     
     def _is_value_nice(self, val):
          if isinstance(val, sp.Rational):
               return True
          return False

     def _calculate_der_expression_as_fraction(self):
          numerator = self.numerator.symbolic_expression
          denominator = self.denominator.symbolic_expression
          der_numerator_exp = sp.expand(sp.diff(numerator)*denominator - sp.diff(denominator)*numerator)
          der_denominator_exp = denominator*denominator
          return der_numerator_exp/der_denominator_exp
     
     def calculate_roots(self, decimal_places, show_complex_roots=False):
          roots = sp.solve(self.rational_expression, x)
          if show_complex_roots:
               self.roots = roots
               return self.roots
          real_roots =[]
          for r in roots:
               if r.is_real:
                    if decimal_places is not None:
                         r = round(r, decimal_places)
                    real_roots.append(r)
          self.roots = real_roots
          return real_roots
     
     def calculate_y_intercept(self, decimals):
          for d in self.discontinuities:
               if np.isclose(d, 0):
                    self.y_intercept = None
                    return self.y_intercept
          if decimals is None:
               self.y_intercept = self.function_evaluator(sp.Integer(0))
          else:
               self.y_intercept = round(self.function_evaluator(0), decimals)
          return self.y_intercept

     def calc_and_classify_stationary_points(self, decimal_places=None):
          self.inflection_x_val, inflections, minima, maxima = [], [], [], []
          num_stat_points=0
          solutions = sp.solve(sp.simplify(self.der_expression), x)
          for p in solutions:
               if np.isclose(float(sp.im(p.evalf())), 0):
                    value_is_nice = self._is_value_nice(p)
                    if not value_is_nice:
                         p = p.evalf()
                    second_der_p_value = float(sp.re(self.second_der_evaluator(p)))
                    if np.isclose(second_der_p_value, 0):
                         inflections.append(self._get_point_on_curve(p, decimal_places, value_is_nice))
                         self.inflection_x_val.append(float(sp.re(p)))
                    elif second_der_p_value < 0:
                         maxima.append(self._get_point_on_curve(p, decimal_places, value_is_nice))
                    elif second_der_p_value > 0:
                         minima.append(self._get_point_on_curve(p, decimal_places, value_is_nice))
                    num_stat_points +=1
          self.stat_points = {'Minima': minima, 'Maxima': maxima, 'Stationary inflection points': inflections}
          print("There are " + str(num_stat_points) + " stationary points")
          print("Stationary points are: ", self.stat_points)
          return self.stat_points
     
     def calc_non_stationary_inflection_points(self, decimal_places=None):
          self.inflection_points = []
          num_inflection_points = 0
          solutions = sp.solve(sp.simplify(self.second_der_expression), x)
          for p in solutions:
               if np.isclose(float(sp.im(p.evalf())), 0) and not any(np.isclose(float(sp.re(p.evalf())), self.inflection_x_val)):
                    value_is_nice = self._is_value_nice(p)
                    if value_is_nice:
                         self.inflection_points.append(self._get_point_on_curve(p, decimal_places, value_is_nice))
                    else:
                         self.inflection_points.append(self._get_point_on_curve(p.evalf(), decimal_places))
                    num_inflection_points+=1
          print("There are " + str(num_inflection_points) + " non-stationary inflection points")
          print("Non-stationary inflection points are: ", self.inflection_points)
          return self.inflection_points
     
     def calculate_derivative_coefficients(self, num_coeffs, den_coeffs):
         der_num_coeffs = np.polysub(np.polymul(np.polyder(num_coeffs), den_coeffs), np.polymul(np.polyder(den_coeffs), num_coeffs))
         der_den_coeffs = np.polymul(den_coeffs, den_coeffs)
         return [der_num_coeffs, der_den_coeffs]
     
     def get_function_latex(self, latex_is_simplified):
          if latex_is_simplified:
               return sp.latex(self.rational_expression_simp)
          elif not latex_is_simplified and self.reduces_to_constant:
               return r'\frac{' + sp.latex(self.numerator.symbolic_expression) + r'}{' + sp.latex(self.denominator.symbolic_expression) + r'}'
          return sp.latex(self.rational_expression)

     def get_derivative_latex(self, display_der_as_fraction, latex_is_simplified):
          if display_der_as_fraction:
               numerator = self.numerator.symbolic_expression
               denominator = self.denominator.symbolic_expression
               der_numerator_exp = sp.expand(sp.diff(numerator)*denominator - sp.diff(denominator)*numerator)
               der_denominator_exp = denominator*denominator
               if latex_is_simplified:
                    der_denominator_exp = sp.expand(der_denominator_exp)
                    return sp.latex(sp.simplify(der_numerator_exp/der_denominator_exp))
               return sp.latex(der_numerator_exp/der_denominator_exp)
          if latex_is_simplified:
               return sp.latex(sp.simplify(self.der_expression))
          return sp.latex(self.der_expression)
    

