def interpolate_density(altitudes, densities, target_altitude):
    for i in range(len(altitudes) - 1):
        if altitudes[i] <= target_altitude <= altitudes[i + 1]:
            altitude_range = altitudes[i + 1] - altitudes[i]
            weight_high = (target_altitude - altitudes[i]) / altitude_range
            weight_low = 1 - weight_high
            interpolated_density = weight_low * densities[i] + weight_high * densities[i + 1]
            return interpolated_density

    # If the target_altitude is outside the range of provided altitudes
    return None

altitudes = [6377, 6378, 6379, 6380, 6381, 6382, 6383, 6385, 6387, 6392, 6397, 6402]
densities = [1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5258, 0.4135, 0.1948, 0.08891, 0.04008]

target_altitude = 7000  # Altitude in meters
interpolated_density = interpolate_density(altitudes, densities, target_altitude)

if interpolated_density is not None:
    print(f"The interpolated density at {target_altitude} meters is {interpolated_density:.4f} kg/m³.")
else:
    print("Altitude is outside the range of provided data.")
