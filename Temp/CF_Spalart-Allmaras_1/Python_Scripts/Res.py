import re
import matplotlib.pyplot as plt
import os

def extract_residuals(log_file):
    # Regular expressions to match residual lines
    residual_pattern = re.compile(r"Solving for (\w+), Initial residual = ([\d\.e+-]+), Final residual = ([\d\.e+-]+)")
    
    # Dictionaries to store residuals
    residuals = {}
    iteration = 0
    # Open the log file and parse it
    with open(log_file, 'r') as file:
        for line in file:
            match = residual_pattern.search(line)
            if match:
                field, initial_residual, final_residual = match.groups()
                initial_residual = float(initial_residual)
                final_residual = float(final_residual)
                
                if field not in residuals:
                    residuals[field] = {'initial': [], 'final': [], 'iteration': []}
                
                residuals[field]['initial'].append(initial_residual)
                residuals[field]['final'].append(final_residual)
                residuals[field]['iteration'].append(iteration)
                
            if "Time =" in line:
                iteration += 1
    
    return residuals

# Path to the log file
log_file = '/home/manascfd/Masters_Projects_Main/CF_Ke_1/log.simpleFoam'

# Check if the log file exists
if not os.path.isfile(log_file):
    print(f"File {log_file} does not exist.")
    exit(1)

# Extract residuals from the log file
residuals = extract_residuals(log_file)

# Check if any residuals were extracted
if not residuals:
    print("No residuals were extracted. Check the log file format and the regular expression pattern.")
else:
    # Plot residuals
    plt.figure(figsize=(12, 8))

    for field, res in residuals.items():
        plt.plot(res['iteration'], res['initial'], label=f'Initial residual ({field})')
        plt.plot(res['iteration'], res['final'], label=f'Final residual ({field})')

    plt.yscale('log')
    plt.xlabel('Iteration')
    plt.ylabel('Residual')
    plt.title('Residuals vs Iterations')
    plt.legend()
    plt.grid(True)
    plt.show()
