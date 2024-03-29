from sympy.abc import x
import sympy as sp
import numpy as np

class RationalFunction():

     def __init__(self, numerator, denominator):
          self.numerator_exp = numerator.symbolic_expression
          self.denominator_exp = denominator.symbolic_expression
          num_coeffs = numerator.coefficients
          den_coeffs = denominator.coefficients
          num_degree = numerator.degree
          den_degree = denominator.degree
          if num_degree<den_degree:
               self._set_asymp_bools(True, False, False, False)
               self.non_vert_asymp_latex = '0'
          elif num_degree==den_degree:
               self._set_asymp_bools(False, True, False, False)
               self.non_vert_asymp_latex = sp.latex(sp.simplify(sp.sympify(num_coeffs[0])/sp.sympify(den_coeffs[0])))
          else:
               quotient = sp.div(self.numerator_exp, self.denominator_exp)[0]
               self.non_vert_asymp_latex = sp.latex(quotient)
               self.asymptote_lambda = sp.lambdify(x, quotient, "numpy")
               if num_degree - den_degree == 1:
                    self._set_asymp_bools(False, False, True, False)
               else:
                    self._set_asymp_bools(False, False, False, True)
          
          self.rational_expression = self.numerator_exp/self.denominator_exp
          self.rational_expression_simp = sp.simplify(self.rational_expression)
          self.der_expression = sp.diff(self.rational_expression, x)
          self.der_expression_as_fraction = self._calculate_der_expression_as_fraction(self.numerator_exp, self.denominator_exp)
          self.second_der_expression = sp.diff(self.der_expression, x)
          
          self.reduces_to_constant = self.rational_expression_simp.is_real
          
          if self.reduces_to_constant:
               self.function_evaluator = lambda t : (num_coeffs[0]*t)/(den_coeffs[0]*t)
          elif not self.reduces_to_constant and self.denominator_exp.is_real:
               self.function_evaluator = lambda t : (self._generate_numerator_lambda(num_coeffs, t))/(den_coeffs[0])
          else:
               self.function_evaluator = sp.lambdify(x, self.rational_expression, "numpy")
          self.der_evaluator = sp.lambdify(x, self.der_expression, "numpy") #"numpy" argument gives lambdify function access to numpy functions backed by compiled C code, which makes execution faster (without ~1microsecond, with~10nanoseconds)
          self.second_der_evaluator = sp.lambdify(x, self.second_der_expression, "numpy")
          
          exp = self.rational_expression if not self.denominator_exp.is_Rational and not self.denominator_exp.is_Add else self.rational_expression_simp
          if not self.reduces_to_constant:
               inverted_rational_exp = sp.simplify(1/exp)
               poles = sp.solve(inverted_rational_exp, x)
               discontinuities = []
               symbolic_discontinuities = []
               for p in poles:
                    if p.is_real:
                         symbolic_discontinuities.append(p)
                         discontinuities.append(float(p))
                    self.discontinuities = sorted(discontinuities)
          else:
               self.discontinuities = []
          
          self.asymp_is_vert = False if not self.discontinuities else True
          if self.asymp_is_vert:
               vert_asymp_latex = []
               for d in symbolic_discontinuities:
                    vert_asymp_latex.append(sp.latex(d))
               self.vert_asymp_latex = vert_asymp_latex
     
     def _set_asymp_bools(self, asymp_is_zero_hor, asymp_is_non_zero_hor, asymp_is_oblique, asymp_is_curv):
          self.asymp_is_zero_hor = asymp_is_zero_hor
          self.asymp_is_non_zero_hor = asymp_is_non_zero_hor
          self.asymp_is_oblique = asymp_is_oblique
          self.asymp_is_curv = asymp_is_curv

     def _generate_numerator_lambda(self, numerator, t):
          n = 0
          for coeff in numerator:
               n += coeff*(t**(len(numerator)-numerator.index(coeff)-1))
          return n
     
     def _calculate_der_expression_as_fraction(self, numerator_exp, denominator_exp):
          der_numerator_exp = sp.expand(sp.diff(numerator_exp)*denominator_exp - sp.diff(denominator_exp)*numerator_exp)
          der_denominator_exp = denominator_exp*denominator_exp
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
     
     def _get_point_on_curve(self, x_val, decimal_places, value_is_nice = False):
          if value_is_nice:
               return (sp.re(x_val), sp.re(self.function_evaluator(x_val)))
          return (round(sp.re(x_val), decimal_places), round(sp.re(self.function_evaluator(x_val)), decimal_places))
     
     def _is_value_nice(self, val):
          if isinstance(val, sp.Rational):
               return True
          return False

     def calc_stationary_points(self, decimal_places=None):
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
          print(f'There {'is' if num_stat_points==1 else 'are'} {num_stat_points} stationary point{'' if num_stat_points==1 else 's'}')
          print(f'Stationary points are: {self.stat_points}')
          return self.stat_points
     
     def calc_non_stat_inflec_points(self, decimal_places=None):
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
          print(f'There {'is' if num_inflection_points==1 else 'are'} {num_inflection_points} non-stationary inflection point{'' if num_inflection_points==1 else 's'}')
          print(f'Non-stationary inflection points are: {self.inflection_points}')
          return self.inflection_points
     
     def get_function_latex(self, latex_is_simplified):
          if latex_is_simplified:
               return sp.latex(self.rational_expression_simp)
          elif not latex_is_simplified and self.reduces_to_constant:
               return r'\frac{' + sp.latex(self.numerator_exp) + r'}{' + sp.latex(self.denominator_exp) + r'}'
          return sp.latex(self.rational_expression)

     def get_derivative_latex(self, display_der_as_fraction, latex_is_simplified):
          if display_der_as_fraction:
               numerator = self.numerator_exp
               denominator = self.denominator_exp
               der_numerator_exp = sp.expand(sp.diff(numerator)*denominator - sp.diff(denominator)*numerator)
               der_denominator_exp = denominator*denominator
               if latex_is_simplified:
                    der_denominator_exp = sp.expand(der_denominator_exp)
                    return sp.latex(sp.simplify(der_numerator_exp/der_denominator_exp))
               return sp.latex(der_numerator_exp/der_denominator_exp)
          if latex_is_simplified:
               return sp.latex(sp.simplify(self.der_expression))
          return sp.latex(self.der_expression)
    

