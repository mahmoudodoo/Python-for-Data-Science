
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creating a line plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, '-r', label='Sine wave')
plt.title('Line Plot Example')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend(loc='best')
plt.show()
