import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values,c = y_values, cmap=plt.cm.Blues, edgecolor = 'none', s=40)

plt.title("Square numbers", fontsize = 14)
plt.xlabel("value", fontsize = 14)
plt.ylabel('Square', fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize= 14)

plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches = 'tight')
