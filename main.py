from main_window.main_window_builder import build_main_window
from main_window.graph.curve_figure import update_graph_section, configure_toolbar_buttons
from main_window.curve_label_display.curve_label_figure import update_curve_label, update_derivative_label
from main_window.analytics.analytics_controller import update_analytics_section, update_analytics_section_visiblity
from main_window.options.options_controller import (switch_random_and_manual_options, switch_curvilinear_asymptote_button, switch_rand_coeffs, switch_rand_roots,
                                                    switch_manual_roots, switch_manual_coeffs, reset_update_bools, switch_simplify_bool, switch_plot_asymps_bool, switch_include_curv_bool,
                                                    switch_plot_deriv_bool, switch_plot_roots_bool, switch_plot_stat_points_bool, switch_plot_stat_inflec_bool,
                                                    switch_plot_nonstat_inflec_bool, switch_display_as_decimals_bool, switch_decimal_places_bool, switch_deriv_as_fraction_bool, 
                                                    switch_simplify_der_eq_bool, get_graph_update_bool, get_curve_label_update_bool, get_analytics_update_bool, get_derivative_label_update_bool)
from main_window.graph.graph_section_controller import update_controls, update_progress_message, update_visibility_of_graph_section
from curve.curve_objects_initialiser import initialise_curve_objects, initialise_manual_curve_objects
from main_window.options.manual_input_popup import manual_popup, get_coefficients, get_roots
from main_window.element_keys import *
import PySimpleGUI as sg


def _generate_graph_and_analytics(window, values, is_updating) -> None:
    update_controls(window, disabled = True)
    window.refresh() #refreshing the window prevents click buffering on disabled buttons
    if not is_updating:
        if values[RANDOM_GEN_KEY]:
            initialise_curve_objects(values)
        else:
            if values[MANUAL_COEFFICIENTS_KEY]:
                numerator_coefficients, denominator_coefficients = get_coefficients()
                if (numerator_coefficients is None) or (denominator_coefficients is None):
                    update_progress_message(window, 'Can`t generator graph: Coefficients haven`t been entered')
                    window.refresh()
                    update_controls(window, disabled = False)
                    return 
                initialise_manual_curve_objects(values, numerator_coefficients=numerator_coefficients, denominator_coefficients=denominator_coefficients)
            else:
                numerator_roots, denominator_roots = get_roots()
                if (numerator_roots is None) or (denominator_roots is None):
                    update_progress_message(window, 'Can`t generator graph: Roots haven`t been entered')
                    window.refresh()
                    update_controls(window, disabled = False)
                    return 
                initialise_manual_curve_objects(values, numerator_roots=numerator_roots, denominator_roots=denominator_roots)
        update_progress_message(window, 'Generating and plotting next graph...')
        update_curve_label(window, values[SIMPLIFY_EQ_KEY])
        update_analytics_section_visiblity(window, visible = values[SHOW_NEXT_ANALYTICS_KEY])
        update_analytics_section(window, values)
        update_derivative_label(window, values[DERIVATIVE_AS_FRACTION_KEY], values[SIMPLIFY_DER_EQ_KEY])
        update_graph_section(values, window)
    else:
        update_progress_message(window, 'Updating current graph...')
        graph_needs_updating = get_graph_update_bool()
        curve_label_needs_updating = get_curve_label_update_bool()
        analytics_needs_updating = get_analytics_update_bool()
        derivative_label_needs_updating = get_derivative_label_update_bool()
        if curve_label_needs_updating:
            update_curve_label(window, values[SIMPLIFY_EQ_KEY])
        if analytics_needs_updating:
            update_analytics_section_visiblity(window, visible = values[SHOW_NEXT_ANALYTICS_KEY])
            update_analytics_section(window, values)
        if derivative_label_needs_updating:
            update_derivative_label(window, values[DERIVATIVE_AS_FRACTION_KEY], values[SIMPLIFY_DER_EQ_KEY])
        if graph_needs_updating:
            update_graph_section(values, window)
    update_progress_message(window, 'Done!')
    window.refresh()
    update_controls(window, disabled = False)
    reset_update_bools()

#TODO: implement logging
#TODO: find a more sophisticated way of event handling than a bulky if-elif-elif... statement (current event handling is completely unviable for more complicated applications)
def _handle_event(window, values, event) -> None:
    if event is GEN_KEY:
        _generate_graph_and_analytics(window, values, is_updating = False)
    elif event is UPDATE_KEY:
        _generate_graph_and_analytics(window, values, is_updating = True)
    elif event in (RANDOM_GEN_KEY, MANUAL_GEN_KEY):
        switch_random_and_manual_options(window, values, event)
    elif event is SIMPLIFY_EQ_KEY:
        switch_simplify_bool()
    elif event is PLOT_ASYMP_KEY:
        switch_curvilinear_asymptote_button(window, values)
        switch_plot_asymps_bool()
    elif event is PLOT_CURV_ASYMP_KEY:
        switch_include_curv_bool()
    elif event is PLOT_DERIVATIVE_KEY:
        switch_plot_deriv_bool()
    elif event is PLOT_ROOTS_KEY:
        switch_plot_roots_bool()
    elif event is PLOT_STATIONARY_POINTS_KEY:
        switch_plot_stat_points_bool()
    elif event is PLOT_STAT_INFLEC_POINTS_KEY:
        switch_plot_stat_inflec_bool()
    elif event is PLOT_NON_STAT_INFLEC_POINTS_KEY:
        switch_plot_nonstat_inflec_bool()
    elif event is DISPLAY_AS_DECIMALS_KEY:
        switch_display_as_decimals_bool()
    elif event is DECIMAL_PLACES_SPIN_KEY:
        switch_decimal_places_bool()
    elif event is DERIVATIVE_AS_FRACTION_KEY:
        switch_deriv_as_fraction_bool()
    elif event is SIMPLIFY_DER_EQ_KEY:
        switch_simplify_der_eq_bool()
    elif event is MANUAL_COEFFICIENTS_KEY:
        switch_manual_roots(window, values)
    elif event is MANUAL_ROOTS_KEY:
        switch_manual_coeffs(window, values)
    elif event is INPUT_VALUES_KEY:
        if values[MANUAL_ROOTS_KEY] and ((values[MANUAL_DEN_DEG_SPIN_KEY]==0)or(values[MANUAL_NUM_DEG_SPIN_KEY]==0)):
            sg.popup('The degree of the numerator and denominator can`t be 0 when inputting roots')
        else:
            manual_popup(values)
    elif event is SHOW_GRAPH_KEY:
        update_visibility_of_graph_section(window, visible = True)
    elif event is HIDE_GRAPH_KEY:
        update_visibility_of_graph_section(window, visible = False)
    elif event is SHOW_ANALYTICS_KEY:
        update_analytics_section_visiblity(window, visible = True)
    elif event is HIDE_ANALYTICS_KEY:
        update_analytics_section_visiblity(window, visible = False)
    elif event is RANDOM_COEFFICIENTS_KEY:
        switch_rand_roots(window, values)
    elif event is RANDOM_ROOTS_KEY:
        switch_rand_coeffs(window, values)

def _perform_startup_processes(window) -> None:
    configure_toolbar_buttons()
    update_analytics_section_visiblity(window, visible = False)

def main() -> None:
    window = build_main_window()
    window.Maximize()
    _perform_startup_processes(window)
    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, EXIT_KEY):
            break
        else:
            _handle_event(window, values, event)
    window.close()


if __name__ == "__main__":
    main()