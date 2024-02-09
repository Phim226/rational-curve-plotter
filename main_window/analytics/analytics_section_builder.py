from main_window.element_keys import *
import PySimpleGUI as sg

#TODO: (MAYBE) have each section be collapsible to tailor which information is visible if user wants to practice calculating specific analytics
#TODO: Split asymptote frame into horizontal, vertical, oblique and curvilinear asymptotes

def Collapsible(layout, key, title='', arrows=(sg.SYMBOL_DOWN, sg.SYMBOL_RIGHT), collapsed=False):
    return sg.Column([[sg.T((arrows[1] if collapsed else arrows[0]), enable_events=True, k=key+'BUTTON'),
                       sg.T(title, enable_events=True, key=key+'TITLE')],
                      [sg.pin(sg.Column(layout, key=key, visible=not collapsed, metadata=arrows))]], pad=(0,0))

def format_analytics_layout():
    return [[sg.Frame('Roots', visible = False,  key = ROOTS_FRAME_KEY, layout =[[sg.T('', key = ROOTS_KEY)]])],
                    [sg.Frame('Derivative', visible = False, key = DERIVATIVE_FRAME_KEY, layout =[
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
                    [sg.Frame('y-intercepts', visible = False, key = Y_INTERCEPT_FRAME_KEY, layout =[[sg.T('', key = Y_INTERCEPT_KEY)]])],
                    [sg.Frame('Asymptotes', visible = False, key = ASYMPTOTES_FRAME_KEY, layout =[[sg.T('')]])]
                ]

def build_analytics_section():
    layout = format_analytics_layout()
    return sg.Frame('Analytics', layout = layout, key = ANALYTIC_SEC_KEY, visible = True)
    #return Collapsible(layout, ANALYTIC_SEC_KEY,  'Analytics', collapsed=True)