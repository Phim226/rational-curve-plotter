from main_window.element_keys import *

disabled_colour = 'grey42'

def _switch_random_options(window, disabled) -> None:
    window[RANDOM_COEFFICIENTS_KEY].update(disabled = disabled)
    window[RANDOM_ROOTS_KEY].update(disabled = disabled)
    window[RANDOM_NUM_TITLE_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[RANDOM_NUM_DEG_SPIN_KEY].update(disabled = disabled)
    window[RANDOM_NUM_DEG_TEXT_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[RANDOM_FORCE_NUM_DEG_KEY].update(disabled = disabled)
    window[RANDOM_DEN_TITLE_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[RANDOM_DEN_DEG_SPIN_KEY].update(disabled = disabled)
    window[RANDOM_DEN_DEG_TEXT_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[RANDOM_FORCE_DEN_DEG_KEY].update(disabled = disabled)

def _switch_manual_options(window, disabled) -> None:
    window[MANUAL_COEFFICIENTS_KEY].update(disabled = disabled)
    window[MANUAL_ROOTS_KEY].update(disabled = disabled)
    window[MANUAL_NUM_TITLE_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[MANUAL_NUM_DEG_SPIN_KEY].update(disabled = disabled)
    window[MANUAL_NUM_DEG_TEXT_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[MANUAL_DEN_TITLE_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[MANUAL_DEN_DEG_SPIN_KEY].update(disabled = disabled)
    window[MANUAL_DEN_DEG_TEXT_KEY].update(text_color = disabled_colour if disabled else 'white')
    window[INPUT_VALUES_KEY].update(disabled = disabled)

'''
Called either when the 'Randomly generate curve' or 'Input curve parameters manually' boxes are checked
and disables or enables the appropriate option section. 

For example, if 'Randomly generate curve' is unticked and 'Input curve parameters manually' is ticked and 'Randomly generate curve' is pressed
then all of the manual options are disabled and all the random options are enabled. If the same button is then pressed again then
the manual options will be re-enabled and the random options disabled.
'''
def switch_random_and_manual_options(window, values, event) -> None:
    if event is RANDOM_GEN_KEY:
        disabled = values[RANDOM_GEN_KEY]
        window[MANUAL_GEN_KEY].update(value = not disabled)
        _switch_random_options(window, not disabled)
        _switch_manual_options(window, disabled)
    else:
        disabled = values[MANUAL_GEN_KEY]
        window[RANDOM_GEN_KEY].update(value = not disabled) 
        _switch_random_options(window, disabled)
        _switch_manual_options(window, not disabled)
    
def switch_curvilinear_asymptote_button(window, values) -> None:
    window[PLOT_CURV_ASYMP_KEY].update(disabled = not values[PLOT_ASYMP_KEY])

def switch_rand_roots(window, values) -> None:
    window[RANDOM_ROOTS_KEY].update(value = not values[RANDOM_COEFFICIENTS_KEY])

def switch_rand_coeffs(window, values) -> None:
    window[RANDOM_COEFFICIENTS_KEY].update(value = not values[RANDOM_ROOTS_KEY])