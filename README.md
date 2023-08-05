# Top-Percentile-Distributions-Visualiser

This Python script provides a statistical tool for visualising the distributions of two groups and comparing their performance in the top nth percentile. It is especially useful in exploring the effects of different mean scores and percentile cutoffs on the proportions of each group that exceed the cutoff. The script utilises packages such as numpy, scipy, and matplotlib to perform the calculations and visualise the output.

The script prompts the user to enter the following parameters:

- The percentage difference between the means of the two groups.
- The percentage cutoff for determining the top performers.
- Labels for the two groups (optional).

The script then calculates and displays:

- The means of the two groups.
- The proportion of each group that is above the cutoff.
- The ratio of Group 1 to Group 2 in the top nth percentile.

The output is visualised in a two-part figure:

1. The first plot is a line graph showing the probability density functions of the two groups, with a vertical line indicating the score cutoff for the top nth percentile.
2. The second plot is a pie chart showing the percentage of each group that falls within the top nth percentile.

An accompanying text box provides the specific numerical values of the key statistics.

Finally, the visualisation is saved as an 'output.png' file.

## Dependencies

- Python 3.x
- numpy
- scipy
- matplotlib

## Usage

You can run this script from the command line like so:

```bash
python3 visualise_distributions.py
```
The script will then prompt you to enter the necessary input parameters.
