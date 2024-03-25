from main_window.element_keys import *
from main_window.equation_label_plotter import build_label
import curve.curve_objects_initialiser as coi

#TODO: include option for roots to be displayed using unicode square root and imaginary unit (\u221a and \u2148 respectively)

def _order_square_root_string(root_string):
    if 'sqrt' in root_string and (' + ' in root_string or ' - ' in root_string):
        root_component = 'sqrt{'
        root_index = root_string.index(root_component)
        if root_index==1:
            sign_component = ' + '
            root_component = f'\\{root_component}'
        elif root_index==3:
            sign_component = ' - '
            root_component = f'\\{root_component}'
        elif root_index==7:
            sign_component = ' + '
            root_component = r'\frac{' + f'\\{root_component}'
        elif root_index==9:
            sign_component = ' - '
            root_component = r'\frac{' + f'\\{root_component}'
        else:
            return root_string
        i = root_index + 5
        while True:
            next_char = root_string[i]
            if next_char == ' ':
                break
            root_component += next_char
            i += 1
        rational_component = '-' if root_string[i+1]=='-' else ''
        rational_component += root_string[i+3:]
        ordered_string = f'{rational_component}{sign_component}{root_component}'
        return ordered_string 
    return root_string

def _format_string(points, is_asymp_string = False):
    first = True
    sep_char = '\n' if is_asymp_string else ', '
    var = 'x = ' if is_asymp_string else ''
    latex_symbol = '$' if is_asymp_string else ''
    for point in points:
        if first:
            first = False
            string = f'{latex_symbol}{var}{point}{latex_symbol}'
        else:
            string = f'{latex_symbol}{var}{point}{latex_symbol}{sep_char}{string}'
    return string 

def _sort_points_descending(points):
    if (len(points)==0) or (len(points)==1):
        return points
    sorted_points = []
    if isinstance(points[0], tuple): 
        x_values = [x[0] for x in points]
    else:
        x_values = [float(x) for x in points]
    while points:
        max_index = x_values.index(max(x_values))
        x_values.pop(max_index)
        sorted_points.append(points.pop(max_index))
    return sorted_points


def _update_roots_info(window, display_analytics_as_decimals, decimal_places) -> None:
    decimal_places = decimal_places if display_analytics_as_decimals else None
    roots = _sort_points_descending(rational_function.calculate_roots(decimal_places))
    if roots:
        window[ROOTS_KEY].update(value = _format_string(roots))
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
    stat_points = rational_function.calc_stationary_points(decimal_places=decimal_places)
    minima = _sort_points_descending(stat_points.get('Minima'))
    maxima = _sort_points_descending(stat_points.get('Maxima'))
    stat_inflec_points = _sort_points_descending(stat_points.get('Stationary inflection points'))
    if minima:
        window[MINIMA_KEY].update(value = _format_string(minima))
    else:
        window[MINIMA_KEY].update(value = 'There are no minima')
    if maxima:
        window[MAXIMA_KEY].update(value = _format_string(maxima))
    else:
        window[MAXIMA_KEY].update(value = 'There are no maxima')
    if stat_inflec_points:
        window[STAT_INFLEC_POINTS_KEY].update(value = _format_string(stat_inflec_points))
    else:
        window[STAT_INFLEC_POINTS_KEY].update(value = 'There are no stationary inflection points')
    return stat_inflec_points

def _update_non_stat_inflection_points_info(window, decimal_places):
    inflec_points = _sort_points_descending(rational_function.calc_non_stat_inflec_points(decimal_places=decimal_places))
    if inflec_points:
        window[NON_STAT_INFLEC_POINTS_KEY].update(value = _format_string(inflec_points))
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
    exp = rational_function.der_expression_as_fraction if display_der_as_fraction or latex_is_simplified else rational_function.der_expression
    latex = rational_function.get_derivative_latex(display_der_as_fraction, latex_is_simplified)
    build_label(window, key, latex, fontsize=12, fig_height=0.5, fig_width=3.2, variable='y')

def update_asymptote_labels(window, values):
    plot_asymptotes = values[PLOT_ASYMP_KEY]
    inc_curvilinear = values[PLOT_CURV_ASYMP_KEY]
    asymp_is_vert = rational_function.asymp_is_vert
    asymp_is_zero_hor = rational_function.asymp_is_zero_hor
    asymp_is_non_zero_hor = rational_function.asymp_is_non_zero_hor
    asymp_is_oblique = rational_function.asymp_is_oblique
    asymp_is_curv = rational_function.asymp_is_curv
    if plot_asymptotes:
        if asymp_is_vert:
            if len(rational_function.discontinuities)==1:
                fig_height = 0.5
            else: 
                fig_height = 0.75
            vert_asymp_latex = _format_string([_order_square_root_string(l) for l in rational_function.vert_asymp_latex], is_asymp_string=True)
            build_label(window, VERTICAL_ASYMP_KEY, vert_asymp_latex, fontsize=10, fig_height=fig_height, fig_width=1.1, y = -0.025)
        window[VERTICAL_COLUMN_KEY].update(visible = asymp_is_vert)
        non_vert_asymp_key = None
        if asymp_is_zero_hor or asymp_is_non_zero_hor:
            window[HORIZONTAL_COLUMN_KEY].update(visible = True)
            window[OBLIQUE_COLUMN_KEY].update(visible = False)
            window[CURV_COLUMN_KEY].update(visible = False)
            non_vert_asymp_key = HORIZONTAL_ASYMP_KEY
            fig_width = 1.1
        elif asymp_is_oblique:
            window[OBLIQUE_COLUMN_KEY].update(visible = asymp_is_oblique)
            window[HORIZONTAL_COLUMN_KEY].update(visible = not asymp_is_oblique)
            window[CURV_COLUMN_KEY].update(visible = not asymp_is_oblique)
            non_vert_asymp_key = OBLIQUE_ASYMP_KEY
            fig_width = 1.1
        elif asymp_is_curv and inc_curvilinear:
            window[CURV_COLUMN_KEY].update(visible = asymp_is_curv)
            window[HORIZONTAL_COLUMN_KEY].update(visible = not asymp_is_curv)
            window[OBLIQUE_COLUMN_KEY].update(visible = not asymp_is_curv)
            non_vert_asymp_key = CURVILINEAR_ASYMP_KEY
            fig_width = 1.5
        if non_vert_asymp_key is not None:
            build_label(window, non_vert_asymp_key, rational_function.non_vert_asymp_latex, fontsize=10, fig_height=0.5, fig_width=fig_width, variable = 'y')
    else:
        window[VERTICAL_COLUMN_KEY].update(visible = False)
        window[CURV_COLUMN_KEY].update(visible = False)
        window[HORIZONTAL_COLUMN_KEY].update(visible = False)
        window[OBLIQUE_COLUMN_KEY].update(visible = False)
        

    
