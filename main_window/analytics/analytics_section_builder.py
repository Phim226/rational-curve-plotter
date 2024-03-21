from main_window.element_keys import *
import PySimpleGUI as sg

STARTUP_VISIBILITY = True

def _build_asymptotes_frame():
    return sg.Frame('Asymptotes', visible = STARTUP_VISIBILITY, key = ASYMPTOTES_FRAME_KEY, layout =[
                        [sg.pin(sg.Column(visible=False, key = VERTICAL_COLUMN_KEY, layout = [
                                [sg.Frame('Vertical', element_justification = 'center', layout =[[sg.Canvas(key = VERTICAL_ASYMP_KEY, visible = STARTUP_VISIBILITY, size=(20, 10)), sg.Push()]])]
                        ]))],
                        [sg.pin(sg.Column(visible=False, key = HORIZONTAL_COLUMN_KEY, layout = [
                                [sg.Frame('Horizontal', element_justification = 'center', layout =[[sg.Canvas(key = HORIZONTAL_ASYMP_KEY, visible = STARTUP_VISIBILITY, size=(20, 10)), sg.Push()]])]
                        ]))],
                        [sg.pin(sg.Column(visible=False, key = OBLIQUE_COLUMN_KEY, layout = [
                                [sg.Frame('Oblique', element_justification = 'center', layout =[[sg.Canvas(key = OBLIQUE_ASYMP_KEY, visible = STARTUP_VISIBILITY, size=(20, 10)), sg.Push()]])]
                        ]))],
                        [sg.pin(sg.Column(visible=False, key = CURV_COLUMN_KEY, layout = [
                                [sg.Frame('Curvilinear', element_justification = 'center', layout =[[sg.Canvas(key = CURVILINEAR_ASYMP_KEY, visible = STARTUP_VISIBILITY, size=(20, 10)), sg.Push()]])]
                        ]))]
                    ])

def _build_roots_frame():
    return sg.Frame('Roots', visible = STARTUP_VISIBILITY,  key = ROOTS_FRAME_KEY, layout =[[sg.T('', key = ROOTS_KEY)]])

def _build_y_intercept_frame():
    return sg.Frame('y-intercept', visible = STARTUP_VISIBILITY, key = Y_INTERCEPT_FRAME_KEY, layout =[[sg.T('', key = Y_INTERCEPT_KEY)]])

def _build_derivative_frame():
    return sg.Frame('Derivative', visible = STARTUP_VISIBILITY, key = DERIVATIVE_FRAME_KEY, layout =[
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
                    ])
def _format_analytics_layout():
    return [[_build_roots_frame(), _build_y_intercept_frame()],
            [sg.vtop(_build_derivative_frame()), sg.vtop(_build_asymptotes_frame())]
        ]

def build_analytics_section():
    layout = _format_analytics_layout()
    return sg.Frame('Analytics', layout = layout, key = ANALYTIC_SEC_KEY, visible = STARTUP_VISIBILITY)