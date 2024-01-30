from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main_window.element_keys import *
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
def build_curve_label_figure(window, curve_latex):
    plt.close()
    text = plt.text(-0.05, -0.01, '$y='+curve_latex+'$', fontsize=16)
    text.set_backgroundcolor(window.BackgroundColor)
    text.get_figure().set_figheight(0.6)
    text.get_figure().set_figwidth(2.2)
    ax = plt.gca()
    ax.set_facecolor(window.BackgroundColor)
    ax.autoscale_view('tight')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.subplots_adjust(left = 0.0, right = 1.0, bottom = 0.0, top = 1.0) #removes white border around graph

def update_curve_label(window, curve_latex):
    window[CURVE_LABEL_KEY].update(visible = True)
    build_curve_label_figure(window, curve_latex)
    text_fig = plt.gcf()
    draw_text_figure(window[CURVE_LABEL_KEY].TKCanvas, text_fig)
