from main_window.main_window_builder import build_main_window
from main_window.graph.curve_figure import update_graph_section, configure_toolbar_buttons
from main_window.curve_label_display.curve_label_figure import update_curve_label
from main_window.analytics.analytics_controller import update_analytics_section, update_analytics_section_visiblity
from main_window.options.options_controller import (switch_random_and_manual_options, switch_curvilinear_asymptote_button, switch_rand_coeffs, 
                                                    switch_rand_roots)
from main_window.graph.graph_section_controller import update_controls, update_progress_message, update_visibility_of_graph_section
from curve.curve_objects_initialiser import initialise_curve_objects
from main_window.element_keys import *
import PySimpleGUI as sg


#TODO: implement logging
#TODO: add event where if update graph button is pressed then the same graph is plotted again with current window values
#TODO: find a more sophisticated way of event handling than a bulky if-elif-elif... statement (current event handling is completely unviable for more complicated applications)
def _handle_event(window, values, event) -> None:
    if event is GEN_KEY:
        update_controls(window, disabled = True)
        window.refresh() #refreshing the window prevents click buffering on disabled buttons
        initialise_curve_objects(values)
        update_progress_message(window, 'Generating and plotting next graph...')
        update_graph_section(values, window)
        update_progress_message(window, 'Formatting curve label...')
        update_curve_label(window, values[SIMPLIFY_EQ_KEY])
        update_progress_message(window, 'Updating analytics...')
        update_analytics_section_visiblity(window, visible = values[SHOW_NEXT_ANALYTICS_KEY])
        update_analytics_section(window)
        update_progress_message(window, 'Done!')
        window.refresh()
        update_controls(window, disabled = False)
    elif event in (RANDOM_GEN_KEY, MANUAL_GEN_KEY):
        switch_random_and_manual_options(window, values, event)
    elif event is PLOT_ASYMP_KEY:
        switch_curvilinear_asymptote_button(window, values)
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

def _perform_startup_processes(window):
    configure_toolbar_buttons()
    update_analytics_section_visiblity(window, visible = False)

def main() -> None:
    window = build_main_window()
    window.Maximize()
    _perform_startup_processes(window)
    while True:
        event, values = window.read()
        window.bring_to_front
        print(event, values)
        if event in (sg.WIN_CLOSED, EXIT_KEY):
            break
        else:
            _handle_event(window, values, event)
    window.close()


if __name__ == "__main__":
    main()