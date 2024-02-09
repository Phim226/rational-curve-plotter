import numpy as np
import random as ran
import sympy as sp
from sympy.abc import x
import curve.symbol_handler as sh

class RandPolynomial():

    def __init__(self, max_degree=2, force_degree=False, coefficients = [], real_roots = []):
        self.max_degree = max_degree
        self.coefficients = self.format_coeffs(coefficients) if coefficients else self.gen_rand_coeffs(force_degree)
        self.degree = max_degree if force_degree else self.get_degree(self.coefficients)
        self.symbolic_expression = sh.build_poly_exp(self.coefficients, self.degree)

    
    def gen_rand_coeffs(self, force_degree):
        range_upper_bound = self.max_degree+1
        coeffs = np.zeros(range_upper_bound)
        if force_degree:
            while coeffs[0]==0:
                    coeffs = np.fromiter((ran.randint(-10,10) for i in range(range_upper_bound)), int)
            return self.format_coeffs(coeffs.tolist())
        else:
            while np.all(coeffs == 0):
                    coeffs = np.fromiter((ran.randint(-10,10) for i in range(range_upper_bound)), int)
            return self.format_coeffs(coeffs.tolist())
            
    
    #removes leading zeros from coefficients list
    def format_coeffs(self, coeffs): 
        for i in range(len(coeffs)):
             if coeffs[i]!=0:
                  coeffs = coeffs[i:]
                  break
        return coeffs
    
    def get_degree(self, coeffs):
        return len(coeffs)-1
    
    def get_symbolic_roots(self, symbolic_expression):
        roots = sp.solve(symbolic_expression, x)
        print(roots)
        for r in roots:
             for i in r.atoms(sp.Pow):
                  print(i)  
        return roots

    def get_real_roots(self,symbolic_roots):
         real_roots = []
         for r in symbolic_roots:
              if r.is_real:
                   real_roots.append(r)
         return sorted(real_roots)
