# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 00:57:51 2024

@author: 22100852
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Load the data from the CSV file
salary_data = pd.read_csv('data2.csv', header=None)
salary_data.columns = ['Annual_Salary']

# Calculate the mean annual salary (W_tilde)
mean_salary = salary_data['Annual_Salary'].mean()

# Create a probability density function using Gaussian kernel density estimation
density_function = gaussian_kde(salary_data['Annual_Salary'])
xs = np.linspace(salary_data['Annual_Salary'].min(), salary_data['Annual_Salary'].max(), 200)

# Plot the histogram and the density function with a customized theme
plt.figure(figsize=(10, 6))
plt.hist(salary_data['Annual_Salary'], bins=30, density=True, alpha=0.5, color='skyblue', edgecolor='black', label='Salary Histogram')
plt.plot(xs, density_function(xs), label='Probability Density Function', color='orange')

# Add mean salary to the plot
plt.axvline(mean_salary, color='red', linestyle='dashed', linewidth=2, label=f'Mean (W_tilde): {mean_salary:.2f}')

# Calculate and plot the value X (95th Percentile)
percentile_95 = np.percentile(salary_data['Annual_Salary'], 95)
plt.axvline(percentile_95, color='green', linestyle='dashed', linewidth=2, label=f'X (95th Percentile): {percentile_95:.2f}')

# Labeling the plot
plt.title('Annual Salary Distribution with Mean and X (95th Percentile)')
plt.xlabel('Annual Salary')
plt.ylabel('Density')
plt.legend()

# Save the plot to a file with a personalized name
plt.savefig('22100852_salary_distribution.png')

# Output the mean annual salary and X
print(f"The mean annual salary (W_tilde) is: {mean_salary:.2f}")
print(f"X (95th Percentile) is: {percentile_95:.2f}")
