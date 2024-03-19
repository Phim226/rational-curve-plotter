from main_window.element_keys import *

disabled_colour = 'grey42'
simplify_has_changed = False
plot_asymps_has_changed = False
include_curv_has_changed = False
plot_deriv_has_changed = False
plot_roots_has_changed = False
plot_stat_points_has_changed = False
plot_stat_inflec_has_changed = False
plot_nonstat_inflec_has_changed = False
display_as_decimals_has_changed = False
decimal_places_has_changed = False
deriv_as_fraction_has_changed = False
simplify_der_has_changed = False

def _switch_random_options(window, disabled) -> None:
    window[RANDOM_COEFFICIENTS_KEY].update(disabled = disabled)
    window[RANDOM_ROOTS_KEY].update(disabled = disabled)
    window[RANDOM_NUM_TITLE_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[RANDOM_NUM_DEG_SPIN_KEY].update(disabled = disabled)
    window[RANDOM_NUM_DEG_TEXT_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[RANDOM_FORCE_NUM_DEG_KEY].update(disabled = disabled)
    window[RANDOM_DEN_TITLE_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[RANDOM_DEN_DEG_SPIN_KEY].update(disabled = disabled)
    window[RANDOM_DEN_DEG_TEXT_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[RANDOM_FORCE_DEN_DEG_KEY].update(disabled = disabled)
    window[EXCLUDE_CONSTANT_KEY].update(disabled = disabled)

def _switch_manual_options(window, disabled) -> None:
    window[MANUAL_COEFFICIENTS_KEY].update(disabled = disabled)
    window[MANUAL_ROOTS_KEY].update(disabled = disabled)
    window[MANUAL_NUM_TITLE_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[MANUAL_NUM_DEG_SPIN_KEY].update(disabled = disabled)
    window[MANUAL_NUM_DEG_TEXT_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[MANUAL_DEN_TITLE_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[MANUAL_DEN_DEG_SPIN_KEY].update(disabled = disabled)
    window[MANUAL_DEN_DEG_TEXT_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[INPUT_VALUES_KEY].update(disabled = disabled)

def switch_random_and_manual_options(window, values, event) -> None:
    if event is RANDOM_GEN_KEY:
        disabled = values[RANDOM_GEN_KEY]
        window[MANUAL_GEN_KEY].update(value = not disabled)
        _switch_random_options(window, not disabled)
        _switch_manual_options(window, disabled)
    else:
        disabled = values[MANUAL_GEN_KEY]
        window[RANDOM_GEN_KEY].update(value = not disabled) 
        _switch_random_options(window, disabled)
        _switch_manual_options(window, not disabled)
    
def switch_curvilinear_asymptote_button(window, values) -> None:
    window[PLOT_CURV_ASYMP_KEY].update(disabled = not values[PLOT_ASYMP_KEY])

def switch_rand_roots(window, values) -> None:
    window[RANDOM_ROOTS_KEY].update(value = not values[RANDOM_COEFFICIENTS_KEY])

def switch_rand_coeffs(window, values) -> None:
    window[RANDOM_COEFFICIENTS_KEY].update(value = not values[RANDOM_ROOTS_KEY])

def switch_manual_roots(window, values) -> None:
    window[MANUAL_ROOTS_KEY].update(value = not values[MANUAL_COEFFICIENTS_KEY])

def switch_manual_coeffs(window, values) -> None:
    window[MANUAL_COEFFICIENTS_KEY].update(value = not values[MANUAL_ROOTS_KEY])

def reset_update_bools() -> None:
    global simplify_has_changed, plot_asymps_has_changed, include_curv_has_changed, plot_deriv_has_changed, plot_roots_has_changed, plot_stat_points_has_changed
    global plot_stat_inflec_has_changed, plot_nonstat_inflec_has_changed, display_as_decimals_has_changed, decimal_places_has_changed, deriv_as_fraction_has_changed, simplify_der_has_changed
    simplify_has_changed = False
    plot_asymps_has_changed = False
    include_curv_has_changed = False
    plot_deriv_has_changed = False
    plot_roots_has_changed = False
    plot_stat_points_has_changed = False
    plot_stat_inflec_has_changed = False
    plot_nonstat_inflec_has_changed = False
    display_as_decimals_has_changed = False 
    decimal_places_has_changed = False
    deriv_as_fraction_has_changed = False
    simplify_der_has_changed = False

def switch_simplify_bool() -> None:
    global simplify_has_changed
    simplify_has_changed = not simplify_has_changed

def switch_plot_asymps_bool() -> None:
    global plot_asymps_has_changed
    plot_asymps_has_changed = not plot_asymps_has_changed

def switch_include_curv_bool() -> None:
    global include_curv_has_changed
    include_curv_has_changed = not include_curv_has_changed

def switch_plot_deriv_bool() -> None:
    global plot_deriv_has_changed
    plot_deriv_has_changed = not plot_deriv_has_changed

def switch_plot_roots_bool() -> None:
    global plot_roots_has_changed
    plot_roots_has_changed = not plot_roots_has_changed

def switch_plot_stat_points_bool() -> None:
    global plot_stat_points_has_changed
    plot_stat_points_has_changed = not plot_stat_points_has_changed

def switch_plot_stat_inflec_bool() -> None:
    global plot_stat_inflec_has_changed
    plot_stat_inflec_has_changed = not plot_stat_inflec_has_changed

def switch_plot_nonstat_inflec_bool() -> None:
    global plot_nonstat_inflec_has_changed
    plot_nonstat_inflec_has_changed = not plot_nonstat_inflec_has_changed

def switch_display_as_decimals_bool() -> None:
    global display_as_decimals_has_changed
    display_as_decimals_has_changed = not display_as_decimals_has_changed

def switch_decimal_places_bool() -> None:
    global decimal_places_has_changed
    decimal_places_has_changed = not decimal_places_has_changed if not decimal_places_has_changed else decimal_places_has_changed

def switch_deriv_as_fraction_bool() -> None:
    global deriv_as_fraction_has_changed
    deriv_as_fraction_has_changed = not deriv_as_fraction_has_changed

def switch_simplify_der_eq_bool() -> None:
    global simplify_der_has_changed
    simplify_der_has_changed = not simplify_der_has_changed

def get_graph_update_bool():
    pa = plot_asymps_has_changed
    ic = include_curv_has_changed
    pd = plot_deriv_has_changed
    pr = plot_roots_has_changed
    psp = plot_stat_points_has_changed
    psi = plot_stat_inflec_has_changed
    pnsi = plot_nonstat_inflec_has_changed
    graph_needs_updating = pa or ic or pd or pr or psp or psi or pnsi
    return graph_needs_updating

def get_curve_label_update_bool():
    return simplify_has_changed

def get_analytics_update_bool():
    return display_as_decimals_has_changed or decimal_places_has_changed

def get_derivative_label_update_bool():
    return deriv_as_fraction_has_changed or simplify_der_has_changed