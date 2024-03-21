import numpy as np
import random as ran
import sympy as sp
from sympy.abc import x

class RandPolynomial():

    def __init__(self, max_degree = 2, force_degree = False, random_coefficients = False, random_roots = False, coefficients = [], real_roots = []):
        self.max_degree = max_degree
        if random_coefficients:
            self.coefficients = self._gen_random_coeffs(force_degree)
        elif coefficients:
            self.coefficients = self._format_coeffs(coefficients)
        elif random_roots:
            self.real_roots = self._gen_random_roots(force_degree)
            self.coefficients = self._get_coeffs_from_roots(self.real_roots)
        elif not random_roots and real_roots:
             self.real_roots = real_roots
             self.coefficients = self._get_coeffs_from_roots(self.real_roots)
        self.degree = max_degree if force_degree else self._get_degree(self.coefficients)
        self.symbolic_expression = self._build_poly_exp_from_coeffs(self.coefficients, self.degree)

    def _gen_random_roots(self, force_degree):
        all_possible_roots = [r for r in range(-3, 4)]
        roots = []
        i = 0
        if force_degree:
            while i < self.max_degree:
                index = ran.randint(0, len(all_possible_roots)-1)
                roots.append(all_possible_roots[index])
                i+=1
            return roots
        all_possible_roots.append(None)
        while not roots:
            while i < self.max_degree:
                index = ran.randint(0, len(all_possible_roots)-1)
                root = all_possible_roots[index]
                if root is None:
                    i+=1 
                    continue
                roots.append(root)
                i+=1
        return roots          
              
    def _gen_random_coeffs(self, force_degree):
        range_upper_bound = self.max_degree+1
        coeffs = np.zeros(range_upper_bound)
        if force_degree:
            while coeffs[0]==0:
                    coeffs = np.fromiter((ran.randint(-10,10) for i in range(range_upper_bound)), int)
            return self._format_coeffs(coeffs.tolist())
        while np.all(coeffs == 0):
                coeffs = np.fromiter((ran.randint(-10,10) for i in range(range_upper_bound)), int)
        return self._format_coeffs(coeffs.tolist())
            
    def _build_poly_exp_from_roots(self, roots):
        exp = 1
        for r in roots:
            exp = exp*(x - r)
        exp = sp.expand(exp)
        return exp

    def _get_coeffs_from_roots(self, roots):
        exp = self._build_poly_exp_from_roots(roots)
        poly = sp.Poly(exp, x)
        coeffs = [int(c) for c in poly.all_coeffs()]
        return coeffs

    def _build_poly_exp_from_coeffs(self, coeffs, degree):
        exp = 0
        for i in range(degree+1):
            exp+=coeffs[i]*(x**(degree-i))
        return exp

    #removes leading zeros from coefficients list
    def _format_coeffs(self, coeffs): 
        for i in range(len(coeffs)):
             if coeffs[i]!=0:
                  coeffs = coeffs[i:]
                  break
        return coeffs
    
    def _get_degree(self, coeffs):
        return len(coeffs)-1