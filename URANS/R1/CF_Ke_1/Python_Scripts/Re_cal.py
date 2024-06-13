import numpy as np
import os
import matplotlib.pyplot as plt

# Parameters
D = 1  # Diameter of the cylinder
nu = 1e-5  # Kinematic viscosity

# Path to the postProcessing directory
postProcessingDir = 'postProcessing/sampleDict'

# Initialize lists to store time steps and Reynolds numbers
time_steps = []
Re_values = []

# Loop through all directories in postProcessing/sampleDict
for time_step in sorted(os.listdir(postProcessingDir)):
    time_step_path = os.path.join(postProcessingDir, time_step)
    
    # Only process directories that are multiples of 100
    try:
        time_step_value = float(time_step)
        if time_step_value % 100 != 0:
            continue
    except ValueError:
        continue  # Skip if the directory name is not a number
    
    if os.path.isdir(time_step_path):
        # Assuming the .xy file is named sampleLine_U.xy
        sample_file = os.path.join(time_step_path, 'sampleLine_U.xy')
        
        if os.path.exists(sample_file):
            # Load sampled data
            data = np.loadtxt(sample_file)
            
            # Extract velocity magnitude
            U_mag = np.linalg.norm(data[:, 1:], axis=1)
            
            # Calculate average free-stream velocity
            U_inf = np.mean(U_mag)
            
            # Calculate Reynolds number
            Re_D = U_inf * D / nu
            
            # Append to lists
            time_steps.append(time_step_value)
            Re_values.append(Re_D)

# Sort the time steps and corresponding Re values
sorted_indices = np.argsort(time_steps)
time_steps = np.array(time_steps)[sorted_indices]
Re_values = np.array(Re_values)[sorted_indices]

# Plot Reynolds number vs. time step
plt.figure(figsize=(10, 6))
plt.plot(time_steps, Re_values, marker='o')
plt.xlabel('Time Step')
plt.ylabel('Reynolds Number')
plt.title('Reynolds Number vs. Time Step')
plt.grid(True)
plt.show()
