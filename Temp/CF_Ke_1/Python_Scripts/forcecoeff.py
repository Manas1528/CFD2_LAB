import numpy as np
import os
import matplotlib.pyplot as plt

# Parameters
D = 1.0  # Diameter of the cylinder
L = 1.0  # Length of the cylinder (spanwise in 3D case)
rho = 1.0  # Density of the fluid
U_inf = 0.03898  # Free-stream velocity
nu = 1e-5  # Kinematic viscosity

# Path to the postProcessing directory
postProcessingDir = '/home/manascfd/Masters_Projects_Main/CF_Kw_1/postProcessing/forceCoeffs/0'

# Check if the directory exists
if not os.path.exists(postProcessingDir):
    print(f"Directory {postProcessingDir} does not exist.")
    exit(1)

# List contents of the directory for debugging
print("Contents of the postProcessing directory:", os.listdir(postProcessingDir))

# Path to the forceCoeffs file
forceCoeffs_file = os.path.join(postProcessingDir, 'coefficient_0.dat')

# Check if the file exists
if not os.path.isfile(forceCoeffs_file):
    print(f"File {forceCoeffs_file} does not exist.")
    exit(1)

# Load data
data = np.loadtxt(forceCoeffs_file, comments='#', delimiter='\t')

# Extract columns (time, Cd, Cl)
time = data[:, 0]
Cd = data[:, 2]  # Assuming Cd is the third column
Cl = data[:, 3]  # Assuming Cl is the fourth column

# Calculate mean drag and lift coefficients
Cd_mean = np.mean(Cd)
Cl_mean = np.mean(Cl)

# Print mean drag and lift coefficients
print(f'Mean Drag Coefficient: {Cd_mean:.4f}')
print(f'Mean Lift Coefficient: {Cl_mean:.4f}')

# Plot drag and lift coefficients over time
plt.figure(figsize=(10, 6))
plt.plot(time, Cd, label='Drag Coefficient (Cd)')
plt.plot(time, Cl, label='Lift Coefficient (Cl)')
plt.xlabel('Time')
plt.ylabel('Coefficient')
plt.title('Drag and Lift Coefficients vs. Time')
plt.grid(True)
plt.legend()
plt.show()