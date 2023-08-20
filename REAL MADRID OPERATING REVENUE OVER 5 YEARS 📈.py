# -*- coding: utf-8 -*-

# -- Sheet --

import matplotlib.pyplot as plt

# Data
years = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23"]
revenue = [757, 715, 653, 722, 843]  # in millions (€)

# Find the index of the minimum and maximum revenue
min_revenue_index = revenue.index(min(revenue))
max_revenue_index = revenue.index(max(revenue))

# Create the plot
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(years, revenue, marker='o')

# Add lines between the points
plt.plot(years, revenue, color='black')

# Remove the grid
plt.grid(False)

# Add annotation with arrow pointing to the minimum revenue
bbox_props = dict(boxstyle="square,pad=0.3", fc="white", ec="black", lw=1)
plt.annotate(f"Lowest Revenue: €{min(revenue)}M ({years[min_revenue_index]})", 
             xy=(min_revenue_index, min(revenue)), xycoords='data',  # Position of the arrow
             xytext=(-70, -45), textcoords='offset points',  # Position of the text
             arrowprops=dict(facecolor='red', arrowstyle="->", color='red'),  # Arrow color
             bbox=bbox_props)  # Add a box around the text

# Add annotation with arrow pointing to the maximum revenue
plt.annotate(f"Highest Revenue: €{max(revenue)}M ({years[max_revenue_index]})", 
             xy=(max_revenue_index, max(revenue)), xycoords='data',  # Position of the arrow
             xytext=(-87, 30), textcoords='offset points',  # Position of the text (adjusted to move left)
             arrowprops=dict(facecolor='red', arrowstyle="->", color='red'),  # Arrow color
             bbox=bbox_props)  # Add a box around the text

# Add title with red color and bold
plt.title("OPERATING REVENUE OVER 5 YEARS", color='red', fontweight='bold')

# Add x and y axis labels
plt.xlabel("Year")
plt.ylabel("Operating Revenue (€ Millions)")

# Add text labels in boxes for each revenue point
for i, rev in enumerate(revenue):
    plt.text(years[i], rev, f"{rev}M", color='black', ha='center', va='bottom', bbox=bbox_props)

# Save the plot as a PNG image
plt.savefig('Real Madrid Operating Revenue.png', dpi=300)

# Display the plot
plt.show()

