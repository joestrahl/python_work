import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active
while True:
    rw = RandomWalk(100000)
    rw.fill_walk()
    
    plt.figure(dpi = 128, figsize =(16,9))
    
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=.6, c = 'aqua')
    plt.scatter(rw.x_values[0], rw.y_values[0], s=10, c='red')
    
    
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
