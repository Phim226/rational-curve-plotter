from main_window.element_keys import *
from main_window.element_tips import *
import PySimpleGUI as sg

#TODO: include options for manually inputting coefficients
#TODO: add option to plot interesting points (roots, y intercept, stationary, inflection)
#TODO: add option to plot derivative alongside regular curve
#TODO: add option for manually inputting roots 
#TODO: add option to randomly generate the roots instead of the coefficients (include tip saying this is recommended for 'easier' practice since roots can then be guessed since they are guaranteed to be integer)
def build_options_section():
    return sg.Frame('Curve Options', 
                            layout = [
                                [sg.Checkbox('Randomly generate curve', default = True, enable_events=True, key=RANDOM_GEN_KEY, tooltip = RAND_GEN_TIP)],
                                [sg.T('Numerator degree:'), 
                                 sg.Spin([i for i in range(0,3)], disabled = True, initial_value=0, key=NUM_DEG_SPIN_KEY), 
                                 sg.Checkbox('Force degree', default = False, enable_events=True, key=FORCE_NUM_DEG_KEY, tooltip = FORCE_DEGREE_TIP_START + 'numerator' + FORCE_DEGREE_TIP_END)],
                                [sg.T('Denominator degree:'), 
                                 sg.Spin([i for i in range(0,3)], disabled = True, initial_value=0, key=DEN_DEG_SPIN_KEY),
                                 sg.Checkbox('Force degree', default = False, enable_events=True, key=FORCE_DEN_DEG_KEY, tooltip = FORCE_DEGREE_TIP_START + 'denominator' + FORCE_DEGREE_TIP_END)],
                                [sg.Checkbox('Plot asymptotes', default = True, enable_events=True, key=PLOT_ASYMP_KEY), 
                                 sg.Checkbox('Include curvilinear asymptotes', default=False, key=PLOT_CURV_ASYMP_KEY, tooltip=CURVE_ASYM_TIP)],
                                [sg.Checkbox('Always show next generated graph', default=True, key=SHOW_NEXT_GEN_KEY)]
                            ])