import numpy as np
import matplotlib.pyplot as plt

year = np.linspace(1990,2015,6)
china = [1.1352, 1.2049, 1.2626, 1.3037, 1.3377, 1.3712]
india = [0.8732, 0.9639, 1.0566, 1.1476, 1.2343, 1.3102]

plt.plot(year, china, 'r--', linewidth=2, label="China")
plt.plot(year, india, 'g-.', linewidth=2, label="India")
plt.legend()
plt.title("Total Population of China and India from 1990 to 2015")

plt.xlabel("Year")
plt.ylabel("Billions")
plt.show()