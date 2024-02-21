import numpy as np
import matplotlib.pyplot as plt
import curve.curve_objects_initialiser as coi

#global variables 
x_lims = [-5000, 5000] #the graph is not plotted for x values past these limits
delta = 0.0000001 #small value so that curve is evaluated close but not equal to discontinuities 
data_points = 300000 #number of data points plotted for each graph section and curvilinear asymptote. Greater numbers tends to cause noticeably slow execution

def define_global_variables() -> None:
    global numerator, denominator, rational_function, num_coeffs, den_coeffs, discontinuities
    numerator = coi.numerator
    denominator = coi.denominator
    rational_function = coi.rational_function
    num_coeffs = numerator.coefficients
    den_coeffs = denominator.coefficients
    discontinuities = rational_function.discontinuities

"""
Adjusts the limits of the y-axis depending on the minimum and maximum values of the curve, or sets them to a default of -10 and 10
"""
#TODO: improve decision making about initial y and x axis limits so that, apart from extreme cases, all graph sections are visible when first displaying the graph
def _adjust_yaxis(domains, eval) -> None:
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
def _adjust_xaxis() -> None:
    x_lims_init = [-10, 10]
    if len(discontinuities)==0:
        plt.xlim((x_lims_init[0],x_lims_init[1]))
    else:
        if min(discontinuities)<-10:
            x_lims_init[0] = min(discontinuities)-5
        if len(discontinuities)>1 and max(discontinuities)>10:
            x_lims_init[1] = max(discontinuities)+5
        plt.xlim((x_lims_init[0],x_lims_init[1]))

def plot_asymptotes(plot_curv_asymps) -> None:
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
        if num_degree - den_degree==1:
            X = np.linspace(x_lims[0], x_lims[1], 2)
            plt.plot(X, A(X), color="red",  linewidth=1.5, linestyle="dashed")
        elif plot_curv_asymps:
            X = np.linspace(x_lims[0], x_lims[1], data_points)
            plt.plot(X, A(X), color="red",  linewidth=1.5, linestyle="dashed")

def _plot_graph_section(x_min, x_max, eval, domains) -> None:
    X = np.linspace(x_min+delta, x_max-delta, data_points)
    plt.plot(X, eval(X), color="black",  linewidth=2, linestyle="-")
    domains.append(X)

def plot_curve() -> None:
    _adjust_xaxis()
    eval = rational_function.function_evaluator
    #Graph has to be split into various separate sections to account for vertical asymptotes
    domains = []
    x_min = x_lims[0]
    if discontinuities:
        for d in discontinuities:
            _plot_graph_section(x_min, d, eval, domains) #sections before last discontinuity
            x_min = d
        _plot_graph_section(d, x_lims[1], eval, domains) #section after last discontinuity
    else:
        _plot_graph_section(x_lims[0], x_lims[1], eval, domains)
    _adjust_yaxis(domains, eval)