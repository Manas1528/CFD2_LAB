import numpy as np
import matplotlib.pyplot as plt

# Load the data
spectra_M_data = np.loadtxt('/mnt/data/spectra_M.dat')
vel_profile_data = np.loadtxt('/mnt/data/vel_profile.dat')

# Extract radial coordinates and streamwise velocities
radii = vel_profile_data[:, 0]
streamwise_velocities = vel_profile_data[:, 1]

# Estimate turbulent kinetic energy k from spectra_M.dat
# Assuming spectral values represent energy contributions for each mode
modes = spectra_M_data[:, 0]
spectral_values = spectra_M_data[:, 1]
k_total = np.sum(spectral_values)  # Simplified assumption

# Use the profile data to understand the distribution along the radial direction
# Here we assume k is evenly distributed for simplicity
k_profile = np.full_like(radii, k_total)

# Define the characteristic length scale lc (using pipe radius or another characteristic length)
lc = np.max(radii)  # Simplified assumption, use the maximum radial distance as characteristic length

# Empirical parameter CD
CD = 0.08

# Calculate epsilon using Prandtl's modification
epsilon_profile = CD * (k_profile**(3/2)) / lc

# Calculate omega
omega_profile = epsilon_profile / k_profile

# Plot k, epsilon, and omega as functions of wall distance (radii)
plt.figure(figsize=(15, 5))

# Plot k
plt.subplot(1, 3, 1)
plt.plot(radii, k_profile, marker='o', linestyle='-')
plt.xlabel('Wall Distance (Radial Coordinate)')
plt.ylabel('Turbulent Kinetic Energy (k)')
plt.title('Turbulent Kinetic Energy Profile')
plt.grid(True)

# Plot epsilon
plt.subplot(1, 3, 2)
plt.plot(radii, epsilon_profile, marker='o', linestyle='-', color='r')
plt.xlabel('Wall Distance (Radial Coordinate)')
plt.ylabel('Turbulent Dissipation Rate (ε)')
plt.title('Turbulent Dissipation Rate Profile')
plt.grid(True)

# Plot omega
plt.subplot(1, 3, 3)
plt.plot(radii, omega_profile, marker='o', linestyle='-', color='g')
plt.xlabel('Wall Distance (Radial Coordinate)')
plt.ylabel('Turbulence Frequency (ω)')
plt.title('Turbulence Frequency Profile')
plt.grid(True)

plt.tight_layout()
plt.show()
