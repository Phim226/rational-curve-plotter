from main_window.element_keys import *

disabled_colour = 'grey42'

def _switch_random_options(window, value) -> None:
    window[RANDOM_COEFFICIENTS_KEY].update(disabled = value)
    window[RANDOM_ROOTS_KEY].update(disabled = value)
    window[RANDOM_NUM_TITLE_KEY].update(text_color = disabled_colour if value else 'white')
    window[RANDOM_NUM_DEG_SPIN_KEY].update(disabled = value)
    window[RANDOM_NUM_DEG_TEXT_KEY].update(text_color = disabled_colour if value else 'white')
    window[RANDOM_FORCE_NUM_DEG_KEY].update(disabled = value)
    window[RANDOM_DEN_TITLE_KEY].update(text_color = disabled_colour if value else 'white')
    window[RANDOM_DEN_DEG_SPIN_KEY].update(disabled = value)
    window[RANDOM_DEN_DEG_TEXT_KEY].update(text_color = disabled_colour if value else 'white')
    window[RANDOM_FORCE_DEN_DEG_KEY].update(disabled = value)

def _switch_manual_options(window, value) -> None:
    window[MANUAL_COEFFICIENTS_KEY].update(disabled = value)
    window[MANUAL_ROOTS_KEY].update(disabled = value)
    window[MANUAL_NUM_TITLE_KEY].update(text_color = disabled_colour if value else 'white')
    window[MANUAL_NUM_DEG_SPIN_KEY].update(disabled = value)
    window[MANUAL_NUM_DEG_TEXT_KEY].update(text_color = disabled_colour if value else 'white')
    window[MANUAL_DEN_TITLE_KEY].update(text_color = disabled_colour if value else 'white')
    window[MANUAL_DEN_DEG_SPIN_KEY].update(disabled = value)
    window[MANUAL_DEN_DEG_TEXT_KEY].update(text_color = disabled_colour if value else 'white')
    window[INPUT_VALUES_KEY].update(disabled = value)

'''
Called either when the 'Randomly generate curve' or 'Input curve parameters manually' boxes are checked
and disables or enables the appropriate option section. 

For example, if 'Randomly generate curve' is unticked and 'Input curve parameters manually' is ticked and 'Randomly generate curve' is pressed
then all of the manual options are disabled and all the random options are enabled. If the same button is then pressed again then
the manual options will be re-enabled and the random options disabled.
'''
def switch_random_and_manual_options(window, values, event) -> None:
    if event is RANDOM_GEN_KEY:
        value = values[RANDOM_GEN_KEY]
        window[MANUAL_GEN_KEY].update(value = not value)
        _switch_random_options(window, not value)
        _switch_manual_options(window, value)
    else:
        value = values[MANUAL_GEN_KEY]
        window[RANDOM_GEN_KEY].update(value = not value) 
        _switch_random_options(window, value)
        _switch_manual_options(window, not value)
    
def switch_curvilinear_asymptote_button(window, values) -> None:
    window[PLOT_CURV_ASYMP_KEY].update(disabled=not values[PLOT_ASYMP_KEY])