from main_window.main_window_builder import build_main_window
from main_window.graph.curve_figure import update_graph_section
from main_window.curve_label_display.curve_label_figure import update_curve_label
from main_window.graph.graph_control_section_builder import update_progress_message
from main_window.element_keys import *
import PySimpleGUI as sg
import curve.symbol_handler as sh

#TODO: add event where if update graph button is pressed then the same graph is plotted again with current window values
#TODO: find a more sophisticated way of event handling than a bulky if-elif-elif... statement (current event handling is completely unviable for more complicated applications)
def handle_event(window, values, event):
    if event is GEN_KEY:
        window[GEN_KEY].update(disabled=True)
        window.refresh()
        update_progress_message(window, 'Generating and plotting next graph...')
        update_graph_section(values, window)
        update_progress_message(window, 'Formatting curve label...')
        update_curve_label(window, sh.curve_latex)
        #TODO: include update_analytics_section function
        update_progress_message(window, vis_bool = False)
        window.refresh()
        window[GEN_KEY].update(disabled=False)
    elif event.startswith(ANALYTIC_SEC_KEY):
        window[ANALYTIC_SEC_KEY].update(visible=not window[ANALYTIC_SEC_KEY].visible) 
        window[ANALYTIC_SEC_KEY+'BUTTON'].update(window[ANALYTIC_SEC_KEY].metadata[0] if window[ANALYTIC_SEC_KEY].visible else window[ANALYTIC_SEC_KEY].metadata[1]) #changes which arrow is visible depending on whether the analytics section has just been opened or closed (metadata holds the arrow symbols here)
    elif event is RANDOM_GEN_KEY:
        window[FORCE_NUM_DEG_KEY].update(disabled=not values[RANDOM_GEN_KEY])
        window[FORCE_DEN_DEG_KEY].update(disabled=not values[RANDOM_GEN_KEY])
        window[NUM_DEG_SPIN_KEY].update(disabled=False)
        window[DEN_DEG_SPIN_KEY].update(disabled=False)
        if values[RANDOM_GEN_KEY]:
            if not values[FORCE_NUM_DEG_KEY]:
                window[NUM_DEG_SPIN_KEY].update(disabled=True)
            if not values[FORCE_DEN_DEG_KEY]:
                window[DEN_DEG_SPIN_KEY].update(disabled=True)
    elif event is FORCE_NUM_DEG_KEY:
        window[NUM_DEG_SPIN_KEY].update(disabled=not values[FORCE_NUM_DEG_KEY])
    elif event is FORCE_DEN_DEG_KEY:
        window[DEN_DEG_SPIN_KEY].update(disabled=not values[FORCE_DEN_DEG_KEY])
    elif event is PLOT_ASYMP_KEY:
        window[CURV_ASYMP_KEY].update(disabled=not values[PLOT_ASYMP_KEY])
    elif event is SHOW_KEY:
        window[TOOLBAR_KEY].update(visible = True)
        window[FIGURE_KEY].update(visible = True)
    elif event is HIDE_KEY:
        window[TOOLBAR_KEY].update(visible = False)
        window[FIGURE_KEY].update(visible = False)



def main():
    window = build_main_window()
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