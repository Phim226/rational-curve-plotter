from main_window.element_keys import *
import PySimpleGUI as sg

#TODO: (GENERAL) format section, give access to analytics about curve
#TODO: (MAYBE) have each section be collapsible to tailor which information is visible if user wants to practice calculating specific analytics
#TODO: Split asymptote frame into horizontal, vertical, oblique and curvilinear asymptotes

def Collapsible(layout, key, title='', arrows=(sg.SYMBOL_DOWN, sg.SYMBOL_RIGHT), collapsed=False):
    return sg.Column([[sg.T((arrows[1] if collapsed else arrows[0]), enable_events=True, k=key+'BUTTON'),
                       sg.T(title, enable_events=True, key=key+'TITLE')],
                      [sg.pin(sg.Column(layout, key=key, visible=not collapsed, metadata=arrows))]], pad=(0,0))

def format_analytics_layout():
    return [[sg.Frame('Roots', layout =[[sg.T('', key = ROOTS_KEY)]])],
                    [sg.Frame('y-intercepts', layout =[[sg.T('', key = Y_INTERCEPT_KEY)]])],
                    [sg.Frame('Stationary points', layout =[[sg.T('', key = STAT_POINTS_KEY)]])],
                    [sg.Frame('Inflection points', layout =[[sg.T('', key = INFLEC_POINTS_KEY)]])],
                    [sg.Frame('Asymptotes', layout =[[sg.T('')]])]
                ]

def build_analytics_section():
    layout = format_analytics_layout()
    return Collapsible(layout, ANALYTIC_SEC_KEY,  'Analytics', collapsed=True)