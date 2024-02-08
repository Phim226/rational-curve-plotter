from main_window.element_keys import *
from main_window.element_tips import *
import PySimpleGUI as sg

def update_progress_message(window, message='', vis_bool=True):
    window[PROG_KEY].update(value = message, visible = vis_bool)

def build_graph_controls():
    return sg.Column([
                [sg.B('Generate', key=GEN_KEY),
                 sg.B('Update graph (currently not working)', key=UPDATE_KEY),
                 sg.B('Show graph', key=SHOW_GRAPH_KEY),
                 sg.B('Hide graph', key=HIDE_GRAPH_KEY), 
                 sg.B('Show analytics', key=SHOW_ANALYTICS_KEY),
                 sg.B('Hide analytics', key=HIDE_ANALYTICS_KEY), 
                 sg.B('Exit', key=EXIT_KEY),
                 sg.T('', visible = False, key = PROG_KEY)]
    ])