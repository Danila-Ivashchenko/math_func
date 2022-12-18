import tailor_rows as t_r
from matplotlib import pyplot as plt
import math

def draw_data(x, y, data_x, data_y):
    plt.ylim(ymax=max(data_y))
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.plot(data_x, data_y, color="blue")
    plt.scatter(x, y, color="red")
    plt.grid("true")
    plt.show()

def visual_tailor_exp(n, x = 0, d = 6, show_primal_function = True):
    y = t_r.tailor_exp(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [t_r.tailor_exp(n, x) for x in data_x]
    if show_primal_function:
        plt.plot(data_x, [math.exp(x) for x in data_x], color="green", label="exp")
    draw_data(x, y, data_x, data_y)

def visual_tailor_sin(n, x = 0, d = 6, show_primal_function = True):
    y = t_r.tailor_sin(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [t_r.tailor_sin(n, x) for x in data_x]
    if show_primal_function:
        plt.plot(data_x, [math.sin(x) for x in data_x], color="green", label="exp")
    draw_data(x, y, data_x, data_y)


def visual_tailor_cos(n, x = 0, d = 6, show_primal_function = True):
    y = t_r.tailor_sin(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [t_r.tailor_cos(n, x) for x in data_x]
    if show_primal_function:
        plt.plot(data_x, [math.cos(x) for x in data_x], color="green", label="exp")
    draw_data(x, y, data_x, data_y)

def visual_tailor_arcsin(n, x = 0, d = 1.5):
    y = t_r.tailor_arcsin(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [t_r.tailor_arcsin(n, x) for x in data_x]

    draw_data(x, y, data_x, data_y)

def visual_tailor_arccos(n, x = 0, d = 1.5):
    y = t_r.tailor_arccos(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [t_r.tailor_arccos(n, x) for x in data_x]

    draw_data(x, y, data_x, data_y)



visual_tailor_arccos(2)

