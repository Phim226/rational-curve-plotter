from main_window.element_keys import *
from main_window.equation_label_plotter import build_label
import curve.curve_objects_initialiser as coi

def update_curve_label(window, label_is_simplified):
    window[CURVE_LABEL_KEY].update(visible = True)
    latex = coi.rational_function.get_function_latex(label_is_simplified)
    key = CURVE_LABEL_KEY
    build_label(window, key, 'y', latex, fontsize=16, fig_height=0.6, fig_width=2.2)
