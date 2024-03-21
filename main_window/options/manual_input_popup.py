from main_window.element_keys import *
import PySimpleGUI as sg

superscripts = ['\N{SUPERSCRIPT ZERO}', '\N{SUPERSCRIPT ONE}', '\N{SUPERSCRIPT TWO}', '\N{SUPERSCRIPT THREE}', '\N{SUPERSCRIPT FOUR}', '\N{SUPERSCRIPT FIVE}']
subscripts = ['\N{SUBSCRIPT ONE}', '\N{SUBSCRIPT TWO}', '\N{SUBSCRIPT THREE}', '\N{SUBSCRIPT FOUR}', '\N{SUBSCRIPT FIVE}', ]
numerator_coefficients = None
numerator_roots = None
denominator_coefficients = None
denominator_roots = None

def _format_popup(popup_type_text, numerator_inputs, denominator_inputs):
    return sg.Window(f'Input {popup_type_text}',
                     [[sg.Text(f'Numerator {popup_type_text}', font = 'Helvetica 9 bold underline')],
                      numerator_inputs,
                      [sg.Text(f'Denominator {popup_type_text}', font = 'Helvetica 9 bold underline')],
                      denominator_inputs,
                      [sg.OK(), sg.Cancel()]
                      ])

def _format_inputs(degree, is_num, is_super):
    inputs = []
    frac_component = '_NUMERATOR_' if is_num else '_DENOMINATOR_'
    ran = range(0, degree+1) if is_super else range(0,degree)
    script = superscripts if is_super else subscripts
    gen_type = 'COEFFICIENTS' if is_super else 'ROOTS'
    for i in ran:
            inputs.append(sg.Text(f'x'+script[i]+':'))
            inputs.append(sg.Input('', size = 4, enable_events=True, key = f'INPUT{frac_component}{gen_type}{i}'))
    return inputs

def _set_coefficients(numerator_values, denominator_values):
    global numerator_coefficients, denominator_coefficients
    numerator_coefficients, denominator_coefficients = numerator_values, denominator_values

def _set_roots(numerator_values, denominator_values):
    global numerator_roots, denominator_roots
    numerator_roots, denominator_roots = numerator_values, denominator_values
            
def manual_popup(values):
    numerator_degree = values[MANUAL_NUM_DEG_SPIN_KEY]
    denominator_degree = values[MANUAL_DEN_DEG_SPIN_KEY]
    is_coefficients = values[MANUAL_COEFFICIENTS_KEY]
    gen_type = 'coefficients' if is_coefficients else 'roots'
    numerator_inputs = _format_inputs(numerator_degree, is_num = True, is_super = is_coefficients)
    denominator_inputs = _format_inputs(denominator_degree, is_num = False, is_super = is_coefficients)
    window = _format_popup(gen_type, numerator_inputs, denominator_inputs)
    while True:
        event, vals = window.read()
        print(event, vals)
        if event in (sg.WIN_CLOSED, 'Cancel'):
            _set_coefficients(None, None)
            _set_roots(None, None)
            break
        elif event.startswith('INPUT'):
            if not vals[event]=='':
                if vals[event][-1] not in ('0123456789- '):
                    sg.popup(f'Only integer {gen_type} are allowed')
                    window[event].update(vals[event][:-1])
        elif event == 'OK': 
            numerator_values, denominator_values = [],[]
            all_values_entered = False
            i = 0
            for v in vals:
                if vals.get(v)=='':
                    all_values_entered = False
                    sg.popup(f'Not all {gen_type} have been entered')
                    break
                else:
                    try:
                        value = int(vals.get(v))
                    except:
                        all_values_entered = False
                        sg.popup(f'Some {gen_type} are in an invalid format')
                        break
                    add_value_to_numerator = (i <= numerator_degree) if is_coefficients else (i < numerator_degree)
                    if add_value_to_numerator:
                        numerator_values.append(value)
                    else:
                        denominator_values.append(value)
                    i += 1
                    all_values_entered = True
            if all_values_entered:
                if is_coefficients:
                    _set_coefficients(numerator_values, denominator_values)
                else:
                    _set_roots(numerator_values, denominator_values)
                break
    window.close()

def get_coefficients():
    return [numerator_coefficients, denominator_coefficients]

def get_roots():
    return [numerator_roots, denominator_roots]