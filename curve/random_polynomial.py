import numpy as np
import random as ran
import sympy as sp
from sympy.abc import x
import curve.symbol_handler as sh

class RandPolynomial():

    def __init__(self, max_degree = 2, force_degree = False, random_coefficients = False, random_roots = False, coefficients = [], real_roots = []):
        self.max_degree = max_degree
        if random_coefficients:
            self.coefficients = self.gen_random_coeffs(force_degree)
        elif coefficients:
            self.coefficients = self.format_coeffs(coefficients)
        elif random_roots:
            self.real_roots = self.gen_random_roots(force_degree)
            self.coefficients = sh.get_coeffs_from_roots(self.real_roots)
        self.degree = max_degree if force_degree else self.get_degree(self.coefficients)
        self.symbolic_expression = sh.build_poly_exp_from_coeffs(self.coefficients, self.degree)

    def gen_random_roots(self, force_degree):
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
              
    
    def gen_random_coeffs(self, force_degree):
        range_upper_bound = self.max_degree+1
        coeffs = np.zeros(range_upper_bound)
        if force_degree:
            while coeffs[0]==0:
                    coeffs = np.fromiter((ran.randint(-10,10) for i in range(range_upper_bound)), int)
            return self.format_coeffs(coeffs.tolist())
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
