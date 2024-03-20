from main_window.element_keys import *
from main_window.element_tips import *
import PySimpleGUI as sg

def build_graph_controls():
    return sg.Column([
                [sg.B('Generate', key=GEN_KEY),
                 sg.B('Update', key=UPDATE_KEY, disabled = True, tooltip = UPDATE_TIP),
                 sg.B('Show graph', disabled = True, key=SHOW_GRAPH_KEY),
                 sg.B('Hide graph', disabled = True, key=HIDE_GRAPH_KEY), 
                 sg.B('Show analytics', disabled = True, key=SHOW_ANALYTICS_KEY),
                 sg.B('Hide analytics', disabled = True, key=HIDE_ANALYTICS_KEY), 
                 sg.B('Exit', key=EXIT_KEY),
                 sg.T('', visible = False, key = PROG_KEY)]
    ])