from matplotlib import pyplot as plt
import numpy as np 
# Median Developer Salaries by Age
dev_x = np.array([25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])

dev_y = np.array([38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752])

plt.plot(dev_x, dev_y, label='All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(dev_x, py_dev_y, label='Python')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title("Median Salary (USD) by Age")
plt.legend(loc='upper left')
plt.show()
