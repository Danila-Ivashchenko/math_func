from matplotlib import pyplot as plt
from approximation import lower_square_method, linear_approximation

def show_graph(x, y):
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

def visual_lower_square_method(data):
    plt.title("Interpolation for point")

    point_x = lower_square_method(data)
    if (len(point_x) == 1):
        point_x = point_x[0]
        point_y = point_x * data[0][0]
    else:
        point_y = point_x[1]
        point_x = point_x[0]
    print(point_x, point_y)

    plt.scatter(point_x, point_y, color="orange")
    x = [point_x + i for i in range(-10, 11)]
    y = [x[i] for i in range(len(x))]
    plt.scatter(x, y, color='blue')
    show_graph(x, y)

def visual_linear_approximation(data_xy, x):
    plt.title("Interpolation for point")

    point_x = x
    point_y =[item[1] for item in linear_approximation(data_xy, x)]

    x = [linear_approximation(data_xy, [i])[0] for i in range(min(point_x) - 10, max(point_x) + 10)]
    y = [linear_approximation(data_xy, x[i])[1] for i in range(len(x))]


    plt.scatter([item[0] for item in data_xy], [item[1] for item in data_xy], color='blue')


    plt.scatter(point_x, point_y, color="orange")

    show_graph(x, y)

data_ay = [[2, 4], [3, 9]]
data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
visual_linear_approximation(data_xy, [3, 5])