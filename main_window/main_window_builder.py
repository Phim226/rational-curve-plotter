from main_window.options.options_section_builder import build_options_section
from main_window.curve_label_display.curve_label_section_builder import build_curve_label_section
from main_window.graph.graph_control_section_builder import build_graph_controls
from main_window.graph.graph_section_builder import build_graph_section
from main_window.analytics.analytics_section_builder import build_analytics_section
import PySimpleGUI as sg

def build_main_window():
    options = build_options_section()
    curve_label = build_curve_label_section()
    graph_control = build_graph_controls()
    graph = build_graph_section()
    analytics = build_analytics_section()
    layout = [[sg.Column([
                [options], 
                [graph_control], 
                [sg.vtop(sg.Column([[curve_label],[analytics]])), graph]], pad = (0,0)),
              ]]
    return sg.Window('Rational curve plotter', layout, resizable=True).Finalize()