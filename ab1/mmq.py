import numpy as np

radius = np.array([6377, 6378, 6379, 6380, 6381, 6382, 6383, 6385, 6387, 6392, 6397, 6402])
density = np.array([1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5258, 0.4135, 0.1948, 0.08891, 0.04008])

# Convert radius to altitude in kilometers
altitude = 6371 - radius

# Fit a linear polynomial (1st degree) to the data
fit_coefficients = np.polyfit(altitude, density, 1)

# Get the slope (variation of density with altitude)
density_variation = fit_coefficients[0]

# Calculate the density at 7000 m altitude using the linear fit
target_altitude = 7  # Convert 7000 meters to kilometers
target_density = np.polyval(fit_coefficients, 6371 - target_altitude)

print("Variation of density with altitude:", density_variation)
print("Density at 7000 m altitude:", target_density)
