from curve.random_polynomial import RandPolynomial
from curve.rational_function import RationalFunction
import numpy as np
import matplotlib.pyplot as plt
import curve.curve_objects_initialiser as coi

#global variables 
x_lims = [-5000, 5000] #the graph is not plotted for x values past these limits
delta = 0.0000001 #small value so that curve is evaluated close but not equal to values where the denominator is 0 
data_points = 300000 #number of data points plotted for each graph section and curvilinear asymptote. Greater numbers tends to cause noticeably slow execution

def define_global_variables():
    global numerator, denominator, rational_function, num_coeffs, den_coeffs, discontinuities
    numerator = coi.numerator
    denominator = coi.denominator
    rational_function = coi.rational_function
    num_coeffs = numerator.coefficients
    den_coeffs = denominator.coefficients
    discontinuities = rational_function.discontinuities

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
    if len(discontinuities)==0:
        plt.xlim((x_lims_init[0],x_lims_init[1]))
    else:
        if min(discontinuities)<-10:
            x_lims_init[0] = min(discontinuities)-5
        if len(discontinuities)>1 and max(discontinuities)>10:
            x_lims_init[1] = max(discontinuities)+5
        plt.xlim((x_lims_init[0],x_lims_init[1]))

def plot_asymptotes():
    num_coeffs, num_degree = numerator.coefficients, numerator.degree
    den_coeffs, den_degree = denominator.coefficients, denominator.degree
    for z in discontinuities:
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

def plot_graph_section(x_min, x_max, eval, domains):
    X = np.linspace(x_min+delta, x_max-delta, data_points)
    plt.plot(X, eval(X), color="black",  linewidth=2, linestyle="-")
    domains.append(X)

def plot_curve():
    adjust_xaxis()
    #TODO: change where curve_latex is generated (probably in class itself)
    curve_latex = rational_function.format_function_label()
    eval = rational_function.function_evaluator
    #Graph has to be split into various separate sections to account for vertical asymptotes
    domains = []
    x_min = x_lims[0]
    if discontinuities:
        for d in discontinuities:
            plot_graph_section(x_min, d, eval, domains) #sections before last discontinuity
            x_min = d
        plot_graph_section(d, x_lims[1], eval, domains) #section after last discontinuity
    else:
        plot_graph_section(x_lims[0], x_lims[1], eval, domains)
    adjust_yaxis(domains, eval)