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
def _adjust_yaxis(domains, eval, reduces_to_constant) -> None:
    ylim_low = -10.0
    ylim_high = 10.0
    if reduces_to_constant:
        plt.ylim((ylim_low,ylim_high))
    else:
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
    for z in discontinuities:
        plt.axvline(z, color = "red", linestyle = "dashed")
    if rational_function.asymp_is_zero_hor:
        plt.axhline(0, color = "red", linestyle = "dashed")
    elif rational_function.asymp_is_non_zero_hor:
        plt.axhline(num_coeffs[0]/den_coeffs[0], color = "red", linestyle = "dashed")
    else:
        A = rational_function.asymptote_lambda
        if rational_function.asymp_is_oblique:
            X = np.linspace(x_lims[0], x_lims[1], 2)
            plt.plot(X, A(X), color="red",  linewidth=1.5, linestyle="dashed")
        elif plot_curv_asymps:
            X = np.linspace(x_lims[0], x_lims[1], data_points)
            plt.plot(X, A(X), color="red",  linewidth=1.5, linestyle="dashed")
    plt.plot([], [], color = 'red', linestyle='dashed', label = 'Asymptotes')

def _plot_graph_section(x_min, x_max, eval, domains, colour, data_points = data_points, label = None) -> None:
    X = np.linspace(x_min+delta, x_max-delta, data_points)
    plt.plot(X, eval(X), color=colour,  linewidth=2, linestyle="-", label = label)
    domains.append(X)

def plot_curve(plot_derivative) -> None:
    _adjust_xaxis()
    eval = rational_function.function_evaluator if not plot_derivative else rational_function.der_evaluator
    colour = 'black' if not plot_derivative else 'blue'
    label = None if not plot_derivative else 'Derivative'
    reduces_to_constant = rational_function.reduces_to_constant
    domains = []
    x_min = x_lims[0]
    if not reduces_to_constant:
        if discontinuities:
            #Graph has to be split into various separate sections to account for vertical asymptotes
            for d in discontinuities:
                _plot_graph_section(x_min, d, eval, domains, colour) #sections before last discontinuity
                x_min = d
            _plot_graph_section(d, x_lims[1], eval, domains, colour, label = label) #section after last discontinuity
        else:
            _plot_graph_section(x_lims[0], x_lims[1], eval, domains, colour, label = label)
    else:
        _plot_graph_section(x_lims[0], x_lims[1], eval, domains, colour, 2 , label = label)
    _adjust_yaxis(domains, eval, reduces_to_constant)

def plot_point(point, colour, label = None) -> None:
    plt.scatter(point[0], point[1], color = colour, label = label)