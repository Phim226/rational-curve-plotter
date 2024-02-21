from main_window.element_keys import *
from main_window.element_tips import *
import PySimpleGUI as sg

def build_graph_controls():
    return sg.Column([
                [sg.B('Generate', key=GEN_KEY),
                 sg.B('Update graph', key=UPDATE_KEY),
                 sg.B('Show graph', key=SHOW_GRAPH_KEY),
                 sg.B('Hide graph', key=HIDE_GRAPH_KEY), 
                 sg.B('Show analytics', key=SHOW_ANALYTICS_KEY),
                 sg.B('Hide analytics', key=HIDE_ANALYTICS_KEY), 
                 sg.B('Exit', key=EXIT_KEY),
                 sg.T('', visible = False, key = PROG_KEY)]
    ])