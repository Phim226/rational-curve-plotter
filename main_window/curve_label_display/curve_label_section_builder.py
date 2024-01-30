from main_window.element_keys import *
import PySimpleGUI as sg

def build_curve_label_section():
    return sg.Frame('Curve',
                            layout = [
                                [sg.Canvas(key=CURVE_LABEL_KEY, visible=False)]
                            ])