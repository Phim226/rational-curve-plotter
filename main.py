from main_window.main_window_builder import build_main_window
from main_window.graph.curve_figure import update_graph_section, configure_toolbar_buttons
from main_window.curve_label_display.curve_label_figure import update_curve_label
from main_window.analytics.analytics_controller import update_analytics_section, update_analytics_section_visiblity
from main_window.options.options_controller import (switch_random_and_manual_options, switch_curvilinear_asymptote_button, switch_rand_coeffs, 
                                                    switch_rand_roots, reset_update_bools, switch_simplify_bool, switch_plot_asymps_bool, switch_include_curv_bool,
                                                    switch_plot_deriv_bool, switch_plot_roots_bool, switch_plot_stat_points_bool, switch_plot_stat_inflec_bool,
                                                    switch_plot_nonstat_inflec_bool, switch_display_as_decimals_bool, switch_decimal_places_bool, 
                                                    get_graph_update_bool, get_curve_label_update_bool, get_analytics_update_bool)
from main_window.graph.graph_section_controller import update_controls, update_progress_message, update_visibility_of_graph_section
from curve.curve_objects_initialiser import initialise_curve_objects
from main_window.element_keys import *
import PySimpleGUI as sg


def _generate_graph_and_analytics(window, values, is_updating) -> None:
    update_controls(window, disabled = True)
    window.refresh() #refreshing the window prevents click buffering on disabled buttons
    if not is_updating:
        initialise_curve_objects(values)
        update_progress_message(window, 'Generating and plotting next graph...')
        update_graph_section(values, window)
        update_progress_message(window, 'Formatting curve label and calculating analytics...')
        update_curve_label(window, values[SIMPLIFY_EQ_KEY])
        update_analytics_section_visiblity(window, visible = values[SHOW_NEXT_ANALYTICS_KEY])
        update_analytics_section(window, values)
    else:
        update_progress_message(window, 'Updating current graph...')
        graph_needs_updating = get_graph_update_bool()
        curve_label_needs_updating = get_curve_label_update_bool()
        analytics_needs_updating = get_analytics_update_bool()
        if graph_needs_updating:
            update_graph_section(values, window)
        if curve_label_needs_updating:
            update_curve_label(window, values[SIMPLIFY_EQ_KEY])
        if analytics_needs_updating:
            update_analytics_section_visiblity(window, visible = values[SHOW_NEXT_ANALYTICS_KEY])
            update_analytics_section(window, values)
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
    elif event is PLOT_STAT_INFLEC_POINTS:
        switch_plot_stat_inflec_bool()
    elif event is PLOT_NON_STAT_INFLEC_POINTS:
        switch_plot_nonstat_inflec_bool()
    elif event is DISPLAY_AS_DECIMALS_KEY:
        switch_display_as_decimals_bool()
    elif event is DECIMAL_PLACES_SPIN_KEY:
        switch_decimal_places_bool()
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