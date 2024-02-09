from main_window.element_keys import *
from main_window.element_tips import *
import PySimpleGUI as sg

disabled_colour = 'grey42'

MANUAL_DISABLED_ON_STARTUP = True

def _format_random_options():
    return sg.Column([
        [sg.Checkbox('Randomly generate curve', default = True, enable_events=True, key=RANDOM_GEN_KEY, tooltip = RAND_GEN_TIP)],
        [sg.Checkbox('Random coefficients', default = True, enable_events=True, key = RANDOM_COEFFICIENTS_KEY),
         sg.Checkbox('Random roots', default = False, enable_events=True, key = RANDOM_ROOTS_KEY)],
        [sg.Column(layout =[
            [sg.T('Numerator', key = RANDOM_NUM_TITLE_KEY, font = 'Helvetica 9 bold underline')],
            [sg.T('Degree', key = RANDOM_NUM_DEG_TEXT_KEY, tooltip=RANDOM_DEGREE_SPIN_TIP), 
             sg.Spin([i for i in range(0,3)], initial_value=2, key=RANDOM_NUM_DEG_SPIN_KEY, tooltip=RANDOM_DEGREE_SPIN_TIP)],
            [sg.Checkbox('Force degree', default = False, enable_events=True, key=RANDOM_FORCE_NUM_DEG_KEY, tooltip = FORCE_DEGREE_TIP_START + 'numerator' + FORCE_DEGREE_TIP_END)]
         ]),
         sg.VerticalSeparator(),
         sg.Column(layout =[
            [sg.T('Denominator', key = RANDOM_DEN_TITLE_KEY, font = 'Helvetica 9 bold underline')],
            [sg.T('Degree', key = RANDOM_DEN_DEG_TEXT_KEY, tooltip=RANDOM_DEGREE_SPIN_TIP), 
             sg.Spin([i for i in range(0,3)], initial_value=2, key=RANDOM_DEN_DEG_SPIN_KEY, tooltip=RANDOM_DEGREE_SPIN_TIP)],
            [sg.Checkbox('Force degree', default = False, enable_events=True, key=RANDOM_FORCE_DEN_DEG_KEY, tooltip = FORCE_DEGREE_TIP_START + 'numerator' + FORCE_DEGREE_TIP_END)]
         ])]
    ])

def _format_manual_options():
    return sg.Column([
        [sg.Checkbox('Input curve parameters manually', default = False, enable_events=True, key=MANUAL_GEN_KEY, tooltip = MANUAL_GEN_TIP)],
        [sg.Checkbox('Input coefficients', default = True, disabled = MANUAL_DISABLED_ON_STARTUP, enable_events=True, key = MANUAL_COEFFICIENTS_KEY),
         sg.Checkbox('Input roots', default = False, disabled = MANUAL_DISABLED_ON_STARTUP, enable_events=True, key = MANUAL_ROOTS_KEY)],
        [sg.Column(layout =[
            [sg.T('Numerator', key = MANUAL_NUM_TITLE_KEY, text_color = disabled_colour, font = 'Helvetica 9 bold underline')],
            [sg.T('Degree', text_color = disabled_colour, key = MANUAL_NUM_DEG_TEXT_KEY), 
             sg.Spin([i for i in range(0,3)], disabled = MANUAL_DISABLED_ON_STARTUP, initial_value=0, key=MANUAL_NUM_DEG_SPIN_KEY)]
         ]),
         sg.VerticalSeparator(),
         sg.Column(layout =[
            [sg.T('Denominator', key = MANUAL_DEN_TITLE_KEY, text_color = disabled_colour, font = 'Helvetica 9 bold underline')],
            [sg.T('Degree', text_color = disabled_colour, key = MANUAL_DEN_DEG_TEXT_KEY), 
             sg.Spin([i for i in range(0,3)], disabled = MANUAL_DISABLED_ON_STARTUP, initial_value=0, key=MANUAL_DEN_DEG_SPIN_KEY)]
         ])],
         [sg.B('Input values', disabled = MANUAL_DISABLED_ON_STARTUP, key=INPUT_VALUES_KEY)]
    ])

def _format_misc_options():
    return sg.Column([
        [sg.Checkbox('Plot asymptotes', default = True, enable_events=True, key=PLOT_ASYMP_KEY), 
         sg.Checkbox('Include curvilinear asymptotes', default=False, key=PLOT_CURV_ASYMP_KEY, tooltip=CURVE_ASYM_TIP)],
        [sg.Checkbox('Always show next generated graph', default=True, key=SHOW_NEXT_GEN_KEY)]
    ])

#TODO: include options for manually inputting coefficients
#TODO: add option to plot interesting points (roots, y intercept, stationary, inflection)
#TODO: add option to plot derivative alongside regular curve
#TODO: add option for manually inputting roots 
#TODO: add option to randomly generate the roots instead of the coefficients (include tip saying this is recommended for 'easier' practice since roots can then be guessed since they are guaranteed to be integer)
def build_options_section():
    return sg.Frame('Curve Generation Options', 
                            layout = [
                                 [_format_random_options(),
                                  sg.VerticalSeparator(),
                                  _format_manual_options(),
                                  sg.VerticalSeparator(),
                                  sg.vtop(_format_misc_options())]
                            ])