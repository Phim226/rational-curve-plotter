from main_window.element_keys import *
import curve.curve_objects_initialiser as coi

#TODO: improve formatting of roots, stationary points and inflection points (currently the raw list is displayed)
#TODO: include option for user to choose decimal precision of numbers
#TODO: include option for roots to be displayed using unicode square root and imaginary unit (\u221a and \u2148 respectively)
#TODO: Display derivative function (with formatting options)
#TODO: Display asymptotes 

def _update_roots_info(window):
    roots = rational_function.calculate_roots()
    if roots:
        window[ROOTS_KEY].update(value = roots)
    else:
        window[ROOTS_KEY].update(value = "There are no real roots")

def _update_y_intercept_info(window):
    y_intercept = rational_function.calculate_y_intercept()
    if y_intercept is None:
        window[Y_INTERCEPT_KEY].update(value = "The curve doesn't cross the y-axis")
    else: 
        window[Y_INTERCEPT_KEY].update(value = "Curve crosses the y-axis at y = " + str(y_intercept))

def _update_stationary_points_info(window):
    stat_points = rational_function.calculate_stationary_points()
    if stat_points:
        window[STAT_POINTS_KEY].update(value = stat_points)
    else:
        window[STAT_POINTS_KEY].update(value = 'There are no stationary points')

def _update_inflection_points_info(window):
    inflec_points = rational_function.calculate_inflection_points()
    if inflec_points:
        window[INFLEC_POINTS_KEY].update(value = inflec_points)
    else:
        window[INFLEC_POINTS_KEY].update(value = 'There are no inflection points')

def update_analytics_section(window):
    global rational_function
    rational_function = coi.rational_function
    _update_roots_info(window)
    _update_y_intercept_info(window)
    _update_stationary_points_info(window)
    _update_inflection_points_info(window)
