from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def draw_text_figure(canvas, text_fig):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(text_fig, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def build_label(window, key, latex, fontsize, fig_height, fig_width, x = -0.05, y = -0.01, colour = None):
    plt.close()
    text = plt.text(x, y, latex, fontsize=fontsize, color = colour)
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
    text_fig = plt.gcf()
    draw_text_figure(window[key].TKCanvas, text_fig)