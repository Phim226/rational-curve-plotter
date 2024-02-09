from main_window.element_keys import *
import PySimpleGUI as sg

CURVE_LABEL_CANVAS_SIZE = 60

def build_curve_label_section():
    return sg.Frame('Curve',
                            layout = [
                                [sg.Canvas(key=CURVE_LABEL_KEY, visible=True, size = (CURVE_LABEL_CANVAS_SIZE*3.66, CURVE_LABEL_CANVAS_SIZE))]
                            ])