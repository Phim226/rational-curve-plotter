from main_window.element_keys import *
import PySimpleGUI as sg

#TODO: (GENERAL) format section, give access to analytics about curve
#TODO: (MAYBE) have each section be collapsible to tailor which information is visible if user wants to practice calculating specific analytics
#TODO: Have frames be visible depending on if they are populated with data 
#TODO: Split asymptote frame into horizontal, vertical, oblique and curvilinear asymptotes

def Collapsible(layout, key, title='', arrows=(sg.SYMBOL_DOWN, sg.SYMBOL_RIGHT), collapsed=False):
    return sg.Column([[sg.T((arrows[1] if collapsed else arrows[0]), enable_events=True, k=key+'BUTTON'),
                       sg.T(title, enable_events=True, key=key+'TITLE')],
                      [sg.pin(sg.Column(layout, key=key, visible=not collapsed, metadata=arrows))]], pad=(0,0))

def format_analytics_layout():
    return [[sg.Frame('Roots', layout =[[sg.T('')]])],
                    [sg.Frame('y-intercepts', layout =[[sg.T('')]])],
                    [sg.Frame('Stationary points', layout =[[sg.T('')]])],
                    [sg.Frame('Inflection points', layout =[[sg.T('')]])],
                    [sg.Frame('Asymptotes', layout =[[sg.T('')]])]
                ]

def build_analytics_section():
    layout = format_analytics_layout()
    return Collapsible(layout, ANALYTIC_SEC_KEY,  'Analytics', collapsed=True)