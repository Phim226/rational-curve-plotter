from main_window.element_keys import *
from main_window.equation_label_plotter import build_label
import curve.curve_objects_initialiser as coi

#TODO: include options for exact or approximate values 
#TODO: include option for roots to be displayed using unicode square root and imaginary unit (\u221a and \u2148 respectively)
#TODO: Display asymptotes 

def _format_points_string(points):
    string = ''
    first = True
    for point in points:
        if first:
            first = False
            string = f'{point}'
        else:
            string = f'{point}, {string}'
    return string 

def _update_roots_info(window, display_analytics_as_decimals, decimal_places) -> None:
    decimal_places = decimal_places if display_analytics_as_decimals else None
    roots = rational_function.calculate_roots(decimal_places)
    if roots:
        window[ROOTS_KEY].update(value = _format_points_string(roots))
    else:
        window[ROOTS_KEY].update(value = "There are no real roots")

def _update_y_intercept_info(window, display_analytics_as_decimals, decimal_places) -> None:
    decimal_places = decimal_places if display_analytics_as_decimals else None
    y_intercept = rational_function.calculate_y_intercept(decimal_places)
    if y_intercept is None:
        window[Y_INTERCEPT_KEY].update(value = "The curve doesn't cross the y-axis")
    else: 
        window[Y_INTERCEPT_KEY].update(value = f"Curve crosses the y-axis at y = {y_intercept}")

def _update_stationary_points_info(window, decimal_places) -> None:
    stat_points = rational_function.calc_and_classify_stationary_points(decimal_places=decimal_places)
    minima = stat_points.get('Minima')
    maxima = stat_points.get('Maxima')
    stat_inflec_points = stat_points.get('Stationary inflection points')
    if minima:
        window[MINIMA_KEY].update(value = _format_points_string(minima))
    else:
        window[MINIMA_KEY].update(value = 'There are no minima')
    if maxima:
        window[MAXIMA_KEY].update(value = _format_points_string(maxima))
    else:
        window[MAXIMA_KEY].update(value = 'There are no maxima')
    if stat_inflec_points:
        window[STAT_INFLEC_POINTS_KEY].update(value = _format_points_string(stat_inflec_points))
    else:
        window[STAT_INFLEC_POINTS_KEY].update(value = 'There are no stationary inflection points')
    return stat_inflec_points

def _update_non_stat_inflection_points_info(window, decimal_places):
    inflec_points = rational_function.calc_non_stationary_inflection_points(decimal_places=decimal_places)
    if inflec_points:
        window[NON_STAT_INFLEC_POINTS_KEY].update(value = _format_points_string(inflec_points))
    else:
        window[NON_STAT_INFLEC_POINTS_KEY].update(value = 'There are no non-stationary inflection points')

def update_analytics_section(window, values) -> None:
    global rational_function
    rational_function = coi.rational_function
    display_analytics_as_decimals = values[DISPLAY_AS_DECIMALS_KEY]
    decimal_places = values[DECIMAL_PLACES_SPIN_KEY]
    _update_roots_info(window, display_analytics_as_decimals, decimal_places)
    _update_y_intercept_info(window, display_analytics_as_decimals, decimal_places)
    _update_stationary_points_info(window, decimal_places)
    _update_non_stat_inflection_points_info(window, decimal_places)

def update_analytics_section_visiblity(window, visible) -> None:
    window[ROOTS_FRAME_KEY].update(visible = visible)
    window[DERIVATIVE_FRAME_KEY].update(visible = visible)
    window[Y_INTERCEPT_FRAME_KEY].update(visible = visible)
    window[ASYMPTOTES_FRAME_KEY].update(visible = visible)

def update_derivative_label(window, display_der_as_fraction, latex_is_simplified):
    key = DERIVATIVE_LABEL_KEY
    rational = coi.rational_function
    exp = rational.der_expression_as_fraction if display_der_as_fraction or latex_is_simplified else rational.der_expression
    latex = rational.get_derivative_latex(display_der_as_fraction, latex_is_simplified)
    build_label(window, key, latex, fontsize=12, fig_height=0.5, fig_width=3.2)
