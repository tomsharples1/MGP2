import matplotlib.pyplot as plt
import numpy as np

def is_harmonic(b, k):
    return b**2 < 800 * k #4mk 

# Initialize lists to store coordinates for True and False values
true_coordinates = []
false_coordinates = []

# Loop through values of b and k
for b in range(50, 1000, 50):
    for k in range(50, 1000, 50):
        if is_harmonic(b, k):
            true_coordinates.append([b, k])
        else:
            false_coordinates.append([b, k])

# Convert lists to NumPy arrays for easier indexing
true_coordinates = np.array(true_coordinates)
false_coordinates = np.array(false_coordinates)

# Plot True values in one color and False values in another
plt.scatter(true_coordinates[:, 0], true_coordinates[:, 1], color='blue', label='True')
plt.scatter(false_coordinates[:, 0], false_coordinates[:, 1], color='red', label='False')

# Add labels and legend
plt.title("Pairs of b and k to cause dampened harmonic motion")
plt.xlabel('b')
plt.ylabel('k')
plt.legend()

# Show the plot
plt.show()
