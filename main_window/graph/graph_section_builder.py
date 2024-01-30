from main_window.element_keys import *
import PySimpleGUI as sg

def build_graph_section():
    return sg.Column([[sg.Frame('Graph', 
                            layout = [
                                [sg.Canvas(key=TOOLBAR_KEY, visible=True)],
                                [sg.Canvas(key=FIGURE_KEY, visible=True, size=(400 * 2, 400))]
                            ], pad=(0, 0))]
    ])