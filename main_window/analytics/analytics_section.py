from main_window.element_keys import *
import curve.curve_objects_initialiser as coi

#TODO: improve formatting of roots, stationary points and inflection points (currently the raw list is displayed)
#TODO: include options for exact or approximate values 
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
    print_exact_value = True
    y_intercept = rational_function.calculate_y_intercept(print_exact_value)
    if y_intercept is None:
        window[Y_INTERCEPT_KEY].update(value = "The curve doesn't cross the y-axis")
    else: 
        window[Y_INTERCEPT_KEY].update(value = "Curve crosses the y-axis at y = " + str(y_intercept))

def _update_stationary_points_info(window):
    stat_points = rational_function.calc_and_classify_stationary_points(decimal_places=2)
    minima = stat_points.get('Minima')
    maxima = stat_points.get('Maxima')
    stat_inflec_points = stat_points.get('Stationary inflection points')
    if minima:
        window[MINIMA_KEY].update(value = minima)
    else:
        window[MINIMA_KEY].update(value = 'There are no minima')
    if maxima:
        window[MAXIMA_KEY].update(value = maxima)
    else:
        window[MAXIMA_KEY].update(value = 'There are no maxima')
    if stat_inflec_points:
        window[STAT_INFLEC_POINTS_KEY].update(value = stat_inflec_points)
    else:
        window[STAT_INFLEC_POINTS_KEY].update(value = 'There are no stationary inflection points')
    return stat_inflec_points

def _update_non_stat_inflection_points_info(window):
    inflec_points = rational_function.calc_non_stationary_inflection_points(decimal_places=2)
    if inflec_points:
        window[NON_STAT_INFLEC_POINTS_KEY].update(value = inflec_points)
    else:
        window[NON_STAT_INFLEC_POINTS_KEY].update(value = 'There are no non-stationary inflection points')

def update_analytics_section(window):
    global rational_function
    rational_function = coi.rational_function
    _update_roots_info(window)
    _update_y_intercept_info(window)
    _update_stationary_points_info(window)
    _update_non_stat_inflection_points_info(window)
