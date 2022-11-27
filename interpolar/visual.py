from matplotlib import pyplot as plt
from interpolar import *

def show_graph(x, y):
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

def visual_interpolar_for_point(data, point_x):
    plt.title("Interpolation for point")
    x, y = [], []
    for item in data:
        x += [item[0]]
        y += [item[1]]
    plt.scatter(x, y, color='blue')
    point = interpolar_for_point(data, point_x)

    plt.scatter(point[0], point[1], color="orange")
    show_graph(x, y)

def visual_piece_interpolar(data, input_x):
    plt.title("Piece interpolation")
    x, y = [], []
    data_x, data_y = [], []

    xy = piece_interpolar(data, input_x)
    for item in xy:
        x += [item[0]]
        y += [item[1]]

    for item in data:
        data_x += [item[0]]
        data_y += [item[1]]

    plt.scatter(data_x, data_y, color="blue")

    plt.scatter(x, y, color="orange")
    show_graph(data_x, data_y)


def visual_lagrange(data, point_x):
    plt.title("Lagrange interpolation polynomial")
    data_x, data_y = [], []
    for item in data:
        data_x += [item[0]]
        data_y += [item[1]]

    xy = lagrange_polimom(data, point_x)
    point_y = lagrange_polimom(data, point_x)[1]
    plt.scatter(xy[0], xy[1], color="orange")
    plt.axis([min(data_x) - abs(point_x) - 5, max(data_x) + point_x + 5, min(data_y) - abs(point_y * 1.5) - 5, max(data_y) + abs(point_y * 1.5)])

    x = [i / 10 for i in range((min(data_x) - point_x) * 10, (max(data_x) + point_x) * 10 + 1)]
    y = [lagrange_polimom(data, item)[1] for item in x]

    show_graph(x, y)
