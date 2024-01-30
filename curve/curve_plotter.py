from curve.random_polynomial import RandPolynomial
from curve.rational_function import RationalFunction
import numpy as np
import matplotlib.pyplot as plt

#global variables 
x_lims = [-5000, 5000] #the graph is not plotted for x values past these limits
delta = 0.0000001 #small value so that curve is evaluated close but not equal to values where the denominator is 0 
data_points = 300000 #number of data points plotted for each graph section and curvilinear asymptote. Greater numbers tends to cause noticeably slow execution

def define_global_variables(rational_function, numerator, denominator):
    global num_coeffs, den_coeffs, den_roots
    num_coeffs = numerator.coefficients
    den_coeffs = denominator.coefficients
    den_roots = rational_function.reduced_denominator_roots

def initialise_random_polynomials(num_degree = None, den_degree = None):
    return [RandPolynomial(num_degree), RandPolynomial(den_degree)]

def initialise_curve_objects(**forced_values):
    global numerator, denominator, rational_function
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
    #numerator = RandPolynomial(coefficients=[-9, -1, -7])
    #denominator = RandPolynomial(coefficients=[-2,-9,-7])
    print("numerator coefficients: ", numerator.coefficients)
    print("denominator coefficients: ", denominator.coefficients)
    rational_function = RationalFunction(numerator, denominator)
    define_global_variables(rational_function, numerator, denominator)

"""
Alters the position of the axes - moves them to the centre
"""
def adjust_axes():
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

"""
Adjusts the limits of the y-axis depending on the minimum and maximum values of the curve, or sets them to a default of -10 and 10
"""
#TODO: improve decision making about initial y and x axis limits so that, apart from extreme cases, all graph sections are visible when first displaying the graph
def adjust_yaxis(domains, eval):
    ylim_low = -10.0
    ylim_high = 10.0
    eval_min = min(eval(i).min() for i in domains)
    eval_max = max(eval(i).max() for i in domains)
    if -100 < eval_min < -10:
        ylim_low = eval_min - 2
    elif -10 < eval_min < 0:
        ylim_low = eval_min - 1
    elif 0 < eval_min < ylim_high:
        ylim_low = -1
    if 10 < eval_max < 100:
        ylim_high = eval_max + 2
    elif 0 < eval_max < 10:
        ylim_high = eval_max + 1
    elif ylim_low < eval_max < 0:
        ylim_high = 1
    plt.ylim((ylim_low,ylim_high))

"""
Sets the initial limits of the graph to be x = -10 and x = 10, and adjusts based on position of asymptotes
"""
def adjust_xaxis():
    x_lims_init = [-10, 10]
    if len(den_roots)==0:
        plt.xlim((x_lims_init[0],x_lims_init[1]))
    else:
        if min(den_roots)<-10:
            x_lims_init[0] = min(den_roots)-5
        if len(den_roots)>1 and max(den_roots)>10:
            x_lims_init[1] = max(den_roots)+5
        plt.xlim((x_lims_init[0],x_lims_init[1]))

def plot_asymptotes():
    num_coeffs, num_degree = numerator.coefficients, numerator.degree
    den_coeffs, den_degree = denominator.coefficients, denominator.degree
    for z in den_roots:
        plt.axvline(z, c = "red", ls = "dashed")
    if num_degree<den_degree:
        plt.axhline(0, c = "red", ls = "dashed")
    elif num_degree==den_degree:
        plt.axhline(num_coeffs[0]/den_coeffs[0], c = "red", ls = "dashed")
    elif num_degree>den_degree:
        quotient = np.polydiv(num_coeffs, den_coeffs)[0]
        A = lambda X : np.polyval(quotient, X)
        if den_degree==1:
            X = np.linspace(x_lims[0], x_lims[1], 2)
            plt.plot(X, A(X), color="red",  linewidth=1.5, linestyle="dashed")
        else:
            X = np.linspace(x_lims[0], x_lims[1], data_points)
            plt.plot(X, A(X), color="red",  linewidth=1.5, linestyle="dashed")


def plot_curve():
    adjust_xaxis()
    curve_latex = rational_function.format_function_label()
    eval = rational_function.get_function_evaluator()
    #Graph has to be split into various separate sections to account for vertical asymptotes
    #TODO: tidy up code, and generalise to account for arbitrary numbers of graph sections
    if len(den_roots)==1:
        X1 = np.linspace(x_lims[0], den_roots[0]-delta, data_points)
        X2 = np.linspace(den_roots[0]+delta, x_lims[1], data_points)
        plt.plot(X1, eval(X1), color="black",  linewidth=2, linestyle="-", label="$y="+curve_latex+"$")
        plt.plot(X2, eval(X2), color="black",  linewidth=2, linestyle="-")
        adjust_yaxis([X1, X2], eval)  
    elif len(den_roots)==2:
        X1 = np.linspace(x_lims[0], min(den_roots)-delta, data_points)
        X2 = np.linspace(min(den_roots)+delta, max(den_roots)-delta, data_points)
        X3 = np.linspace(max(den_roots)+delta, x_lims[1], data_points)
        plt.plot(X1, eval(X1), color="black",  linewidth=2, linestyle="-", label="$y="+curve_latex+"$")
        plt.plot(X2, eval(X2), color="black",  linewidth=2, linestyle="-")
        plt.plot(X3, eval(X3), color="black",  linewidth=2, linestyle="-")
        adjust_yaxis([X1, X2, X3], eval)
    else:
        X = np.linspace(x_lims[0], x_lims[1], data_points, endpoint=True)
        plt.plot(X, eval(X), color="black",  linewidth=2, linestyle="-", label="$y="+curve_latex+"$")
        adjust_yaxis([X], eval)

class CurvePlotter():

    x_lims = [-5000, 5000] #the graph is not plotted for x values past these limits
    delta = 0.0000001 #small value so that curve is evaluated close but not equal to values where the denominator is 0 
    data_points = 300000 #number of data points plotted for each graph section and curvilinear asymptote. Greater numbers tends to cause noticeably slow execution

    def __init__(self, numerator, denominator, rational_function, derivative):
        self.numerator = numerator
        self.denominator = denominator
        self.rational_function = rational_function
        self.derivative = derivative
    
    def plot_curve(self, eval, curve_latex):
        adjust_xaxis()
        print(den_roots)
        #Graph has to be split into various separate sections to account for vertical asymptotes
        #TODO: tidy up code, and generalise to account for arbitrary numbers of graph sections
        if len(den_roots)==1:
            X1 = np.linspace(x_lims[0], den_roots[0]-delta, data_points)
            X2 = np.linspace(den_roots[0]+delta, x_lims[1], data_points)
            plt.plot(X1, eval(X1), color="black",  linewidth=2, linestyle="-", label="$y="+curve_latex+"$")
            plt.plot(X2, eval(X2), color="black",  linewidth=2, linestyle="-")
            adjust_yaxis([X1, X2], eval)  
        elif len(den_roots)==2:
            X1 = np.linspace(x_lims[0], min(den_roots)-delta, data_points)
            X2 = np.linspace(min(den_roots)+delta, max(den_roots)-delta, data_points)
            X3 = np.linspace(max(den_roots)+delta, x_lims[1], data_points)
            plt.plot(X1, eval(X1), color="black",  linewidth=2, linestyle="-", label="$y="+curve_latex+"$")
            plt.plot(X2, eval(X2), color="black",  linewidth=2, linestyle="-")
            plt.plot(X3, eval(X3), color="black",  linewidth=2, linestyle="-")
            adjust_yaxis([X1, X2, X3], eval)
        else:
            X = np.linspace(x_lims[0], x_lims[1], data_points, endpoint=True)
            plt.plot(X, eval(X), color="black",  linewidth=2, linestyle="-", label="$y="+curve_latex+"$")
            adjust_yaxis([X], eval)