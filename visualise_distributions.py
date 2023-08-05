#!/usr/bin/python3

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def visualise_distributions(percentage_difference, percentage_cutoff, label_A="Group 1", label_B="Group 2"):
    # Calculate the means for the two groups
    mean_A = 50 + (percentage_difference / 2)
    mean_B = 50 - (percentage_difference / 2)
    std_dev = 10

    # Create the normal distributions for the two groups
    dist_A = norm(loc=mean_A, scale=std_dev)
    dist_B = norm(loc=mean_B, scale=std_dev)

    # Find the cut-off point for each group and calculate the average
    cutoff_A = dist_A.ppf(1 - percentage_cutoff / 100)
    cutoff_B = dist_B.ppf(1 - percentage_cutoff / 100)
    cutoff = (cutoff_A + cutoff_B) / 2

    # Calculate the proportion of each group that is above the cutoff
    proportion_A_above_cutoff = dist_A.sf(cutoff)
    proportion_B_above_cutoff = dist_B.sf(cutoff)

    # Calculate the ratio of Group 1 to Group 2 in the top nth percentile
    ratio = proportion_A_above_cutoff / proportion_B_above_cutoff

    # Print the calculated values
    print(f"{label_A} proportion above cut-off: {proportion_A_above_cutoff * 100:.2f}%")
    print(f"{label_B} proportion above cut-off: {proportion_B_above_cutoff * 100:.2f}%")
    print(f"Ratio of {label_A} to {label_B} in the top {percentage_cutoff}%: {ratio:.2f}")

    # Generate values for the x axis
    x = np.linspace(0, 100, 1000)

    # Generate the corresponding values for the y axis for the two groups
    y_A = dist_A.pdf(x)
    y_B = dist_B.pdf(x)

    # Create the figure and the grid
    fig, axs = plt.subplots(2, 2, figsize=(18, 10), gridspec_kw={'width_ratios': [3, 1]})

    # Create the first plot
    axs[0, 0].plot(x, y_A, label=label_A)
    axs[0, 0].plot(x, y_B, label=label_B)
    axs[0, 0].axvline(x=cutoff, color='r', linestyle='--', label=f'{percentage_cutoff}th percentile cutoff')
    axs[0, 0].set_xlabel('Score')
    axs[0, 0].set_ylabel('Probability Density')
    axs[0, 0].set_title('Distributions for the Two Groups')
    axs[0, 0].legend()

    # Create the second plot
    axs[1, 0].pie([proportion_A_above_cutoff, proportion_B_above_cutoff], labels=[label_A, label_B], autopct='%1.1f%%', startangle=140, colors=['b', 'orange'])
    axs[1, 0].set_title(f'Percentage of Each Group in the Top {percentage_cutoff}%')

    # Add the text box with the statistics
    axs[0, 1].axis('off')
    axs[0, 1].text(0, 0.5, f"{label_A} mean: {mean_A:.2f}\n{label_B} mean: {mean_B:.2f}\nCut-off score: {cutoff:.2f}\n{label_A} proportion above cut-off: {proportion_A_above_cutoff * 100:.2f}%\n{label_B} proportion above cut-off: {proportion_B_above_cutoff * 100:.2f}%\nRatio of {label_A} to {label_B} in the top {percentage_cutoff}%: {ratio:.2f}", fontsize=12)

    # Remove the unused subplot
    fig.delaxes(axs[1,1])

    # Adjust the layout and save the figure before showing it
    plt.tight_layout()
    plt.savefig('output.png')
    plt.show()

# Prompt the user for inputs
percentage_difference = float(input("Enter the percentage difference between the means: "))
percentage_cutoff = float(input("Enter the percentage cutoff: "))
label_A = input("Enter a label for the first group (press enter to use 'Group 1'): ")
label_B = input("Enter a label for the second group (press enter to use 'Group 2'): ")

# Use default labels if none were provided
if label_A == "":
    label_A = "Group 1"
if label_B == "":
    label_B = "Group 2"

# Call the function with the user's inputs
visualise_distributions(percentage_difference, percentage_cutoff, label_A, label_B)
