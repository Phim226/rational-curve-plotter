from main_window.element_keys import *

def update_visibility_of_graph_section(window, visible):
    window[TOOLBAR_KEY].update(visible = visible)
    window[FIGURE_KEY].update(visible = visible)

def update_controls(window, disabled):
    window[GEN_KEY].update(disabled = disabled)
    window[UPDATE_KEY].update(disabled = disabled)
    window[SHOW_GRAPH_KEY].update(disabled = disabled)
    window[HIDE_GRAPH_KEY].update(disabled = disabled)
    window[SHOW_ANALYTICS_KEY].update(disabled = disabled)
    window[HIDE_ANALYTICS_KEY].update(disabled = disabled)

def update_progress_message(window, message='', visible=True):
    window[PROG_KEY].update(value = message, visible = visible)