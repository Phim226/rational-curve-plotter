from main_window.element_keys import *
from main_window.element_tips import *
import PySimpleGUI as sg

disabled_colour = 'grey42'

MANUAL_DISABLED_ON_STARTUP = True

def _build_random_options():
    return sg.Column([
        [sg.Checkbox('Randomly generate curve', default = True, enable_events=True, key=RANDOM_GEN_KEY)],
        [sg.Checkbox('Random coefficients', default = True, enable_events=True, key = RANDOM_COEFFICIENTS_KEY, tooltip = RAND_COEFFS_TIP),
         sg.Checkbox('Random roots', default = False, enable_events=True, key = RANDOM_ROOTS_KEY, tooltip = RAND_ROOTS_TIP)],
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

def _build_manual_options():
    return sg.Column([
        [sg.Checkbox('Input curve parameters manually \n (all options non-functional)', default = False, enable_events=True, key=MANUAL_GEN_KEY)],
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

def _build_misc_options():
    return sg.Column([
        [sg.Checkbox('Always show next generated graph', default = True, key = SHOW_NEXT_GEN_KEY, tooltip = SHOW_NEXT_GEN_TIP)],
        [sg.Checkbox('Simplify curve equation', default = False, enable_events = True, key = SIMPLIFY_EQ_KEY, tooltip = SIMPLIFY_EQ_TIP),
         sg.Checkbox('Exclude graphs that reduce to a constant', default = True, key = EXCLUDE_CONSTANT_KEY)],
        [sg.Checkbox('Plot asymptotes', default = True, enable_events=True, key=PLOT_ASYMP_KEY), 
         sg.Checkbox('Include curvilinear asymptotes', default = False, enable_events = True, key=PLOT_CURV_ASYMP_KEY, tooltip=CURVE_ASYM_TIP)],
        [sg.Checkbox('Plot derivate (nw)', default = False, enable_events = True, key = PLOT_DERIVATIVE_KEY),
         sg.Checkbox('Plot roots (nw)', default = False, enable_events = True, key = PLOT_ROOTS_KEY),
         sg.Checkbox('Plot stationary points (nw)', default = False, enable_events = True, key = PLOT_STATIONARY_POINTS_KEY)],
        [sg.Checkbox('Plot stationary inflection points (nw)', default = False, enable_events = True, key = PLOT_STAT_INFLEC_POINTS),
         sg.Checkbox('Plot non-stationary inflection points (nw)', default = False, enable_events = True, key = PLOT_NON_STAT_INFLEC_POINTS)]
    ])

def _build_analytics_options():
    return sg.Column([
        [sg.Checkbox('Always show analytics', default = True, key = SHOW_NEXT_ANALYTICS_KEY, tooltip = SHOW_NEXT_ANALYTICS_TIP)],
        [sg.Checkbox('Display derivative as single fraction', default = False, enable_events = True, key = DERIVATIVE_AS_FRACTION_KEY)],
        [sg.Checkbox('Simplify derivative equation', default = False, enable_events = True, key = SIMPLIFY_DER_EQ_KEY)],
        [sg.Checkbox('Display all analytics as decimals', default = False, enable_events = True, key = DISPLAY_AS_DECIMALS_KEY, tooltip = ANALYTICS_AS_DECIMALS_TIP)],
        [sg.T('Decimal places', key = DECIMAL_PLACES_KEY, tooltip = DECIMAL_PLACES_TIP), 
         sg.Spin([i for i in range(0,9)], initial_value=2, enable_events = True, key = DECIMAL_PLACES_SPIN_KEY, tooltip = DECIMAL_PLACES_TIP)]
    ])

#TODO: include options for manually inputting coefficients
#TODO: add option to plot interesting points (roots, y intercept, stationary, inflection)
#TODO: add option to plot derivative alongside regular curve
#TODO: add option for manually inputting roots 
def build_options_section():
    return sg.Frame('Curve Generation Options', 
                            layout = [
                                 [_build_random_options(),
                                  sg.VerticalSeparator(),
                                  _build_manual_options(),
                                  sg.VerticalSeparator(),
                                  sg.vtop(_build_misc_options()),
                                  sg.VerticalSeparator(),
                                  sg.vtop(_build_analytics_options())]
                            ])