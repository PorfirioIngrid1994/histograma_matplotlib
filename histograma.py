import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(10, 0.5, 5000)
plt.hist(data)
plt.show()

