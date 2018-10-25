import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth = 6)

# Set chart title and label
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontside = 14)

# Set size of tick labels, 
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()
