from main_window.element_keys import *
import PySimpleGUI as sg

STARTUP_VISIBILITY = True

def build_graph_section():
    return sg.Column([[sg.Frame('Graph', 
                            layout = [
                                [sg.Canvas(key=TOOLBAR_KEY, visible=STARTUP_VISIBILITY)],
                                [sg.Canvas(key=FIGURE_KEY, visible=STARTUP_VISIBILITY, size=(375 * 2, 375))]
                            ], pad=(0, 0))]
    ])