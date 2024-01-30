import numpy as np
import random as ran
import sympy as sp
import curve.symbol_handler as sh

#TODO: convert symbolic root calculation into evaluated roots (symbolic roots are sympy classes, not standard python data types that can be compared/plotted properly)

class RandPolynomial():

    x = sp.symbols('x')
    max_degree = 2

    def __init__(self, forced_degree=None, coefficients = [], real_roots = []):
        self.coefficients = self.format_coeffs(coefficients) if coefficients else self.gen_rand_coeffs(forced_degree)
        self.degree = forced_degree if forced_degree is not None else self.get_degree(self.coefficients)
        self.symbolic_expression = sh.build_poly_exp(self.coefficients, self.degree)
        self.symbolic_real_roots = self.get_symbolic_real_roots(self.symbolic_expression)
        self.real_roots = self.get_real_roots(self.symbolic_real_roots)

    
    def gen_rand_coeffs(self, forced_degree):
        if forced_degree is None:
            range_upper_bound = self.max_degree + 1
            coeffs = np.zeros(range_upper_bound)
            while np.all(coeffs == 0):
                    coeffs = np.fromiter((ran.randint(-10,10) for i in range(range_upper_bound)), int)
            return self.format_coeffs(coeffs.tolist())
        else:
            range_upper_bound = forced_degree+1
            coeffs = np.zeros(range_upper_bound)
            while coeffs[0]==0:
                    coeffs = np.fromiter((ran.randint(-10,10) for i in range(range_upper_bound)), int)
            return self.format_coeffs(coeffs.tolist())
    
    def format_coeffs(self, coeffs): #removes leading zeros from coefficients list
        for i in range(len(coeffs)):
             if coeffs[i]!=0:
                  coeffs = coeffs[i:]
                  break
        return coeffs
    
    def get_degree(self, coeffs):
        return len(coeffs)-1
    
    def get_symbolic_real_roots(self, symbolic_expression):
        roots = sp.solve(symbolic_expression, self.x)
        print(roots)
        return roots

    def get_real_roots(self,symbolic_roots):
         real_roots = []
         for r in symbolic_roots:
              if r.is_real:
                   real_roots.append(r)
         return real_roots
