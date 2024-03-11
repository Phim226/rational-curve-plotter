from main_window.element_keys import *
import PySimpleGUI as sg

STARTUP_VISIBILITY = True

#TODO: Split asymptote frame into horizontal, vertical, oblique and curvilinear asymptotes

def format_analytics_layout():
    return [[sg.Frame('Roots', visible = STARTUP_VISIBILITY,  key = ROOTS_FRAME_KEY, layout =[[sg.T('', key = ROOTS_KEY)]]),
             sg.Frame('y-intercept', visible = STARTUP_VISIBILITY, key = Y_INTERCEPT_FRAME_KEY, layout =[[sg.T('', key = Y_INTERCEPT_KEY)]])],
                    [sg.Frame('Derivative', visible = STARTUP_VISIBILITY, key = DERIVATIVE_FRAME_KEY, layout =[
                        [sg.Canvas(key = DERIVATIVE_LABEL_KEY, visible = True, size=(50, 50))],
                        [sg.Column([[sg.T('Minima:', font = 'Helvetica 9 underline bold')],
                                   [sg.T('', key = MINIMA_KEY)],
                                   [sg.T('Maxima:', font = 'Helvetica 9 underline bold')],
                                   [sg.T('', key = MAXIMA_KEY)]]),
                         sg.VerticalSeparator(pad = (0, 10)),
                         sg.Column([[sg.T('Stationary inflection points:', font = 'Helvetica 9 underline bold')],
                                   [sg.T('', key = STAT_INFLEC_POINTS_KEY)],
                                   [sg.T('Non-stationary inflection points:', font = 'Helvetica 9 underline bold')],
                                   [sg.T('', key = NON_STAT_INFLEC_POINTS_KEY)]])]
                    ])],
                    [sg.Frame('Asymptotes', visible = STARTUP_VISIBILITY, key = ASYMPTOTES_FRAME_KEY, layout =[[sg.T('')]])]
                ]

def build_analytics_section():
    layout = format_analytics_layout()
    return sg.Frame('Analytics', layout = layout, key = ANALYTIC_SEC_KEY, visible = STARTUP_VISIBILITY)