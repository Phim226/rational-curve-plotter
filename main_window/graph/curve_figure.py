from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from main_window.element_keys import *
import curve.curve_objects_initialiser as coi
import curve.curve_plotter as cplot
import matplotlib.pyplot as plt

def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = NavigationToolbar2Tk(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)

#Alters the position of the axes - moves them to the centre
def adjust_axes():
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

def build_curve_figure(values):
    plt.close() #previous figure needs to be closed explicitly otherwise matplotlib stores each generated plot in memory. A runtime warning will appear after 20 graphs are plotted if they aren't closed
    plt.figure(figsize=(10, 6), dpi=80)#figsize sets width/height in inches, dpi is figure resolution in inches (dots-per-inch or pixels-per-inch)
    adjust_axes()
    cplot.define_global_variables()
    plot_asmyptotes = values[PLOT_ASYMP_KEY]
    if plot_asmyptotes and not coi.rational_function.reduces_to_constant:
        cplot.plot_asymptotes()
    cplot.plot_curve()
    plt.grid()
    plt.legend(loc='upper left')
    plt.subplots_adjust(left = 0.0, right = 1.0, bottom = 0.0, top = 1.0) #removes white border around graph

def update_visibility_values(show_next_gen, window):
    window[TOOLBAR_KEY].update(visible = show_next_gen)
    window[FIGURE_KEY].update(visible = show_next_gen)

def update_graph_section(values, window):
    update_visibility_values(values[SHOW_NEXT_GEN_KEY], window)
    build_curve_figure(values)
    fig = plt.gcf()
    DPI = fig.get_dpi()
    fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
    draw_figure_w_toolbar(window[FIGURE_KEY].TKCanvas, fig, window[TOOLBAR_KEY].TKCanvas)