from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main_window.element_keys import *
import curve.curve_objects_initialiser as coi
import matplotlib.pyplot as plt

def draw_text_figure(canvas, text_fig):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(text_fig, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

#TODO: have width be dynamic depending on type of label
def build_curve_label_figure(window, latex, fontsize, fig_height, fig_width):
    plt.close()
    text = plt.text(-0.05, -0.01, '$y='+latex+'$', fontsize=fontsize)
    text.set_backgroundcolor(window.BackgroundColor)
    text.get_figure().set_figheight(fig_height)
    text.get_figure().set_figwidth(fig_width)
    ax = plt.gca()
    ax.set_facecolor(window.BackgroundColor)
    ax.autoscale_view('tight')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.subplots_adjust(left = 0.0, right = 1.0, bottom = 0.0, top = 1.0) #removes white border around graph

def _build_label(window, key, latex, fontsize, fig_height, fig_width):
    build_curve_label_figure(window, latex, fontsize, fig_height, fig_width)
    text_fig = plt.gcf()
    draw_text_figure(window[key].TKCanvas, text_fig)

def update_curve_label(window, label_is_simplified):
    window[CURVE_LABEL_KEY].update(visible = True)
    latex = coi.rational_function.get_function_latex(label_is_simplified)
    key = CURVE_LABEL_KEY
    _build_label(window, key, latex, fontsize=16, fig_height=0.6, fig_width=2.2)

def update_derivative_label(window, display_der_as_fraction, latex_is_simplified):
    key = DERIVATIVE_LABEL_KEY
    latex = coi.rational_function.get_derivative_latex(display_der_as_fraction, latex_is_simplified)
    _build_label(window, key, latex, fontsize=12, fig_height=0.5, fig_width=3.0)