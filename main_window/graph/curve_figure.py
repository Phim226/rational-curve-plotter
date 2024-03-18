from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import backend_bases
from main_window.element_keys import *
import curve.curve_objects_initialiser as coi
import curve.curve_plotter as cplot
import matplotlib.pyplot as plt

#defines the buttons that will appear on the plot toolbar
def configure_toolbar_buttons() -> None:
    backend_bases.NavigationToolbar2.toolitems = (
        ('Home', 'Reset original view', 'home', 'home'),
        ('Back', 'Back to  previous view', 'back', 'back'),
        ('Forward', 'Forward to next view', 'forward', 'forward'),
        (None, None, None, None),
        ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
        ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
        #(None, None, None, None) this section was for subplots
        (None, None, None, None),
      )

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

def _draw_points(values, rational_function):
    plot_roots = values[PLOT_ROOTS_KEY]
    plot_stat_points = values[PLOT_STATIONARY_POINTS_KEY]
    plot_stat_inflec_points = values[PLOT_STAT_INFLEC_POINTS_KEY]
    plot_nonstat_inflec_points = values[PLOT_NON_STAT_INFLEC_POINTS_KEY]
    if plot_roots:
        roots = rational_function.roots
        for root in roots:
            if roots.index(root)==0:
                cplot.plot_point((root, 0), 'magenta', 'Root')
            else:
                cplot.plot_point((root, 0), 'magenta')
    if plot_stat_points:
        minima = rational_function.stat_points.get('Minima')
        maxima = rational_function.stat_points.get('Maxima')
        for minimum in minima:
            if minima.index(minimum)==0:
                cplot.plot_point(minimum, 'green', 'Local minimum')
            else:
                cplot.plot_point(minimum, 'green')
        for maximum in maxima:
            if maxima.index(maximum)==0:
                cplot.plot_point(maximum, 'red', 'Local maximum')
            else:
                cplot.plot_point(maximum, 'red')
    if plot_stat_inflec_points:
        stat_inflec_points = rational_function.stat_points.get('Stationary inflection points')
        for stat_inflec in stat_inflec_points:
            if stat_inflec_points.index(stat_inflec)==0:
                cplot.plot_point(stat_inflec, 'orange', 'Stationary inflection point')
            else:
                cplot.plot_point(stat_inflec, 'orange')
    if plot_nonstat_inflec_points:
        nonstat_inflec_points = rational_function.inflection_points
        for nonstat_inflec in nonstat_inflec_points:
            if nonstat_inflec_points.index(nonstat_inflec)==0:
                cplot.plot_point(nonstat_inflec, 'purple', 'Non-stationary inflection point')
            else:
                cplot.plot_point(nonstat_inflec, 'purple')

def build_curve_figure(values):
    plt.close() #previous figure needs to be closed explicitly otherwise matplotlib stores each generated plot in memory. A runtime warning will appear after 20 graphs are plotted if they aren't closed
    plt.figure(figsize=(10, 6), dpi=80)#figsize sets width/height in inches, dpi is figure resolution in inches (dots-per-inch or pixels-per-inch)
    adjust_axes()
    cplot.define_global_variables()
    rational_function = coi.rational_function
    _draw_points(values, rational_function)
    plot_asmyptotes = values[PLOT_ASYMP_KEY]
    if plot_asmyptotes and not rational_function.reduces_to_constant:
        cplot.plot_asymptotes(values[PLOT_CURV_ASYMP_KEY])
    cplot.plot_curve(plot_derivative=False)
    if values[PLOT_DERIVATIVE_KEY]:
        cplot.plot_curve(plot_derivative=True)
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
    fig.set_size_inches(375 * 2 / float(DPI), 375 / float(DPI))
    draw_figure_w_toolbar(window[FIGURE_KEY].TKCanvas, fig, window[TOOLBAR_KEY].TKCanvas)