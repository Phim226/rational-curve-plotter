from main_window.main_window_builder import build_main_window
from main_window.graph.curve_figure import update_graph_section
from main_window.curve_label_display.curve_label_figure import update_curve_label
from main_window.analytics.analytics_controller import update_analytics_section
from main_window.graph.graph_control_section_builder import update_progress_message
from curve.curve_objects_initialiser import initialise_curve_objects
from main_window.options.options_controller import switch_random_and_manual_options, switch_curvilinear_asymptote_button
from main_window.element_keys import *
import PySimpleGUI as sg


#TODO: implement logging
#TODO: add event where if update graph button is pressed then the same graph is plotted again with current window values
#TODO: find a more sophisticated way of event handling than a bulky if-elif-elif... statement (current event handling is completely unviable for more complicated applications)
def handle_event(window, values, event) -> None:
    if event is GEN_KEY:
        window[GEN_KEY].update(disabled=True)
        window.refresh()
        initialise_curve_objects(values)
        update_progress_message(window, 'Generating and plotting next graph...')
        update_graph_section(values, window)
        update_progress_message(window, 'Formatting curve label...')
        update_curve_label(window)
        update_progress_message(window, 'Updating analytics...')
        update_analytics_section(window)
        update_progress_message(window, vis_bool = False)
        window.refresh()
        window[GEN_KEY].update(disabled=False)
    elif event in (RANDOM_GEN_KEY, MANUAL_GEN_KEY):
        switch_random_and_manual_options(window, values, event)
    elif event is PLOT_ASYMP_KEY:
        switch_curvilinear_asymptote_button(window, values)
    elif event is SHOW_GRAPH_KEY:
        window[TOOLBAR_KEY].update(visible = True)
        window[FIGURE_KEY].update(visible = True)
    elif event is HIDE_GRAPH_KEY:
        window[TOOLBAR_KEY].update(visible = False)
        window[FIGURE_KEY].update(visible = False)
    elif event is SHOW_ANALYTICS_KEY:
        window[ANALYTIC_SEC_KEY].update(visible = True)
    elif event is HIDE_ANALYTICS_KEY:
        window[ANALYTIC_SEC_KEY].update(visible = False)



def main() -> None:
    window = build_main_window()
    window.Maximize()
    while True:
        event, values = window.read()
        window.bring_to_front
        print(event, values)
        if event in (sg.WIN_CLOSED, EXIT_KEY):
            break
        else:
            handle_event(window, values, event)
    window.close()


if __name__ == "__main__":
    main()